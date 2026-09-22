#!/usr/bin/env bash
set -euo pipefail

mode="${1:-check}"
case "$mode" in
  check|export) ;;
  *)
    echo "Usage: $0 [check|export]" >&2
    exit 2
    ;;
esac

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
codex_root="${CODEX_HOME:-${HOME}/.codex}"

automation_ids=(
  readwise-cybersecurity-report
  readwise-threat-intelligence-report
  readwise-generative-ai-report
  readwise-cybersecurity-notebooklm-digest
)

changed=0
for automation_id in "${automation_ids[@]}"; do
  source_file="$codex_root/automations/$automation_id/automation.toml"
  destination_dir="$script_dir/$automation_id"
  destination_file="$destination_dir/automation.toml"

  if [[ ! -f "$source_file" ]]; then
    echo "Missing local automation: $source_file" >&2
    exit 1
  fi

  if [[ "$mode" == "export" ]]; then
    mkdir -p "$destination_dir"
    cp "$source_file" "$destination_file"
    echo "Exported $automation_id"
    continue
  fi

  if [[ ! -f "$destination_file" ]]; then
    echo "Missing repository copy: $destination_file"
    changed=1
  elif ! cmp -s "$source_file" "$destination_file"; then
    echo "Out of sync: $automation_id"
    changed=1
  else
    echo "In sync: $automation_id"
  fi
done

exit "$changed"
