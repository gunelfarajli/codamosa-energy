#!/bin/bash

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}"; )" &> /dev/null && pwd 2> /dev/null; )"

if [ "$#" -lt 6 ]; then
    echo "Usage: $0 modules-csv out-dir argfile searchtime --auth authkeyfile"
    echo "   or: $0 modules-csv out-dir argfile searchtime --replay replayfile"
    exit 1
fi

MODULES_CSV=$1
OUT_BASE_DIR=$2
ARGFILE=$3
SEARCH_TIME=$4
PLAY_OPTION=$5
PLAY_KEY=$6

ARGS="$(cat "$ARGFILE")"

mkdir -p "$OUT_BASE_DIR"
mkdir -p ./emissions
MASTER_LOG="$OUT_BASE_DIR/full_run.log"
ALL_STATS="$OUT_BASE_DIR/all_statistics.csv"

if [[ ! -f "$MODULES_CSV" ]]; then
    echo "CSV file not found: $MODULES_CSV"
    exit 1
fi

if [[ ! -d "$SCRIPT_DIR/../test-apps" ]]; then
    echo "It seems that the directory test-apps does not exist. Run ./start_benchmark_container.sh first."
    exit 1
fi

if [ "$PLAY_OPTION" = "--auth" ]; then
    PLAY_CONFIG="--authorization-key $(cat "$PLAY_KEY")"
elif [ "$PLAY_OPTION" = "--replay" ]; then
    PLAY_CONFIG="--replay-generation-from-file $PLAY_KEY"
else
    echo "Invalid option $PLAY_OPTION"
    exit 1
fi

echo "[$(date)] Starting batch run" | tee -a "$MASTER_LOG"
echo "[$(date)] Modules CSV: $MODULES_CSV" | tee -a "$MASTER_LOG"
echo "[$(date)] Output dir: $OUT_BASE_DIR" | tee -a "$MASTER_LOG"
echo "[$(date)] Search time: $SEARCH_TIME" | tee -a "$MASTER_LOG"

FIRST_STATS_WRITTEN=0

while IFS=, read -r TEST_DIR TEST_MOD || [ -n "$TEST_DIR" ]; do
    [ -z "$TEST_DIR" ] && continue
    [ -z "$TEST_MOD" ] && continue

    TEST_DIR="${TEST_DIR%$'\r'}"
    TEST_MOD="${TEST_MOD%$'\r'}"

    FULL_TEST_DIR="$(dirname "$SCRIPT_DIR")/$TEST_DIR"

    if [[ ! -d "$FULL_TEST_DIR" ]]; then
        echo "[$(date)] Skipping $TEST_MOD: directory not found -> $FULL_TEST_DIR" | tee -a "$MASTER_LOG"
        continue
    fi

    SAFE_MOD_NAME="${TEST_MOD//./_}"
    MODULE_OUT_DIR="$OUT_BASE_DIR/$SAFE_MOD_NAME"
    LOG_FILE="$MODULE_OUT_DIR/run.log"
    mkdir -p "$MODULE_OUT_DIR"

    {
        echo "=================================================="
        echo "[$(date)] Running module: $TEST_MOD"
        echo "Input dir:  $FULL_TEST_DIR"
        echo "Output dir: $MODULE_OUT_DIR"
        echo "=================================================="
    } | tee -a "$MASTER_LOG"

    docker run --rm \
        -v ./emissions:/emissions \
        -v "${FULL_TEST_DIR}:/input:ro" \
        -v "${MODULE_OUT_DIR}:/output" \
        -v "${FULL_TEST_DIR}:/package:ro" \
        codamosa-runner \
        --assertion-generation NONE \
        --project_path /input \
        --module-name "${TEST_MOD}" \
        --output-path /output \
        --maximum_search_time "$SEARCH_TIME" \
        --output_variables TargetModule,Coverage,BranchCoverage,LineCoverage,ParsedStatements,UninterpStatements,ParsableStatements,LLMCalls,LLMQueryTime,LLMStageSavedTests,LLMStageSavedMutants,LLMNeededExpansion,LLMNeededUninterpreted,LLMNeededUninterpretedCallsOnly,RandomSeed,AccessibleObjectsUnderTest,CodeObjects,CoverageTimeline \
        --report-dir /output \
        --coverage_metrics BRANCH,LINE \
        $ARGS $PLAY_CONFIG -v \
        2>&1 | tee "$LOG_FILE" | tee -a "$MASTER_LOG"

    if [[ -f "$MODULE_OUT_DIR/statistics.csv" ]]; then
        echo "[$(date)] Finished: $TEST_MOD" | tee -a "$MASTER_LOG"

        if [ "$FIRST_STATS_WRITTEN" -eq 0 ]; then
            cat "$MODULE_OUT_DIR/statistics.csv" > "$ALL_STATS"
            FIRST_STATS_WRITTEN=1
        else
            tail -n +2 "$MODULE_OUT_DIR/statistics.csv" >> "$ALL_STATS"
        fi
    else
        echo "[$(date)] Warning: statistics.csv not found for $TEST_MOD" | tee -a "$MASTER_LOG"
    fi

done < "$MODULES_CSV"

echo "[$(date)] Batch run complete" | tee -a "$MASTER_LOG"