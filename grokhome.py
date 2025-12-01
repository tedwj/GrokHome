#!/usr/bin/env python3
"""
GrokHome CLI: Safe Agent Runner (v0.1, 2025-11-30).
"""

import argparse
from constitution import GrokConstitution
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="GrokHome: Validate & Run Safe Actions")
    parser.add_argument("--action", required=True, help="Action to validate (e.g., 'fetch repo')")
    parser.add_argument("--consent", action="store_true", help="Explicit consent (Rule 5)")
    parser.add_argument("--stop", action="store_true", help="Emergency stop (Rule 9)")
    args = parser.parse_args()

    if args.stop:
        const = GrokConstitution()
        const.emergency_stop()
        return

    const = GrokConstitution()
    approved, msg = const.validate(args.action, {"consent": args.consent, "verified": True})
    
    print(f"\n=== GrokHome [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ===")
    print(f"Status: {msg}")
    if approved:
        print("Executing safely... (Sim: Action would proceed here—e.g., GitHub fetch.)")
    else:
        print("Halted for safety—review logs.")
    
    print("\nRecent Logs:")
    for log in const.get_logs():
        print(f"  • {log}")

if __name__ == "__main__":
    main()
