import time
import sys

def countdown(minutes: int):
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer_str = f"{mins:02d}:{secs:02d}"
        print(f"\rTime left: {timer_str}", end="")
        time.sleep(1)
        total_seconds -= 1
    
    print("\nTime's up!")


if __name__ == "__main__":
    minutes = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    countdown(minutes)