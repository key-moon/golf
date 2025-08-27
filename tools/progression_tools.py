#!/usr/bin/env python3
import argparse
from datetime import datetime
from public_data import loads_task_scores_progressions, dumps_task_scores_progressions, delete_user_progressions, loads_merged_users, dumps_merged_users

def format_datetime(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d")

def ls_command(sort_by: str = 'last_date'):
    task_scores = loads_task_scores_progressions()
    if not task_scores:
        print("No task score progressions found.")
        return

    # Prepare table data
    table_data = []
    for name, tasks in task_scores.items():
        total_subs = sum(len(subs) for subs in tasks)
        if total_subs == 0:
            continue
        all_dates = [sub['date'] for task_subs in tasks for sub in task_subs]
        first_date = format_datetime(min(all_dates))
        last_date = format_datetime(max(all_dates))
        table_data.append([name, total_subs, first_date, last_date])

    # Sort
    if sort_by == 'name':
        table_data.sort(key=lambda x: x[0])
    elif sort_by == 'submissions':
        table_data.sort(key=lambda x: x[1], reverse=True)
    elif sort_by == 'first_date':
        table_data.sort(key=lambda x: x[2])
    elif sort_by == 'last_date':
        table_data.sort(key=lambda x: x[3], reverse=True)  # Default: latest first

    # Calculate column widths
    col_names = ["Name", "Total Submissions", "First Date", "Last Date"]
    col_widths = [len(col) for col in col_names]
    for row in table_data:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(cell)))

    # Print table header
    header = " | ".join(f"{col:<{col_widths[i]}}" for i, col in enumerate(col_names))
    print(header)
    print("-" * len(header))

    # Print table rows
    for row in table_data:
        row_str = " | ".join(f"{str(cell):<{col_widths[i]}}" for i, cell in enumerate(row))
        print(row_str)

def merge_command(merge_to: str, merge_from: list[str]):
    task_scores = loads_task_scores_progressions()

    if merge_to not in task_scores:
        print(f"Error: merge-to user '{merge_to}' not found.")
        return

    missing_from = [name for name in merge_from if name not in task_scores]
    if missing_from:
        print(f"Error: merge-from users {missing_from} not found.")
        return

    # Show stats before merge
    print("=== Merge Preview ===")
    print(f"Merging into user '{merge_to}'")
    tasks_to = task_scores[merge_to]
    total_subs_to = sum(len(subs) for subs in tasks_to)
    print(f"Current total submissions: {total_subs_to}")

    for name in merge_from:
        tasks_from = task_scores[name]
        total_subs_from = sum(len(subs) for subs in tasks_from)
        print(f"\nUser '{name}':")
        print(f"  Total submissions: {total_subs_from}")
        if total_subs_from > 0:
            all_dates = [sub['date'] for task_subs in tasks_from for sub in task_subs]
            print(f"  First date: {format_datetime(min(all_dates))}")
            print(f"  Last date: {format_datetime(max(all_dates))}")

    # Warning
    print("\nWARNING: This will merge the specified users into the target user.")
    print("The merged users will be removed after merging.")
    confirm = input("Do you want to proceed? (y/N): ")
    if confirm.lower() != 'y':
        print("Merge cancelled.")
        return

    # Perform merge
    for task_num in range(400):
        subs_to = tasks_to[task_num]
        for name in merge_from:
            subs_from = task_scores[name][task_num]
            subs_to.extend(subs_from)
        # Sort by date
        subs_to.sort(key=lambda s: s['date'])
        # Remove duplicates (same date and score)
        unique_subs = []
        seen = set()
        for sub in subs_to:
            key = (sub['date'], sub['score'])
            if key not in seen:
                seen.add(key)
                unique_subs.append(sub)
        tasks_to[task_num] = unique_subs

    # Remove merged users
    for name in merge_from:
        del task_scores[name]

    # Save
    dumps_task_scores_progressions(task_scores)
    new_total_subs = sum(len(subs) for subs in tasks_to)
    print(f"Merge completed. New total submission count: {new_total_subs}")

    # Delete original files
    for name in merge_from:
        delete_user_progressions(name)

    # Add merged users to exclusion list
    merged_users = loads_merged_users()
    merged_users.update(merge_from)
    dumps_merged_users(merged_users)

def main():
    parser = argparse.ArgumentParser(description="Manage task score progressions")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # ls command
    ls_parser = subparsers.add_parser('ls', help='List task score progressions with details')
    ls_parser.add_argument('--sort-by', choices=['name', 'submissions', 'first_date', 'last_date'], default='last_date', help='Sort by field (default: last_date)')

    # merge command
    merge_parser = subparsers.add_parser('merge', help='Merge task score progressions')
    merge_parser.add_argument('merge_to', type=str, help='Target user name to merge into')
    merge_parser.add_argument('merge_from', nargs='+', type=str, help='Source user names to merge from')

    args = parser.parse_args()

    if args.command == 'ls':
        ls_command(args.sort_by)
    elif args.command == 'merge':
        merge_command(args.merge_to, args.merge_from)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()