import time
import sys

def countdown(minutes: int, label: str):
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer_str = f"{mins:02d}:{secs:02d}"
        print(f"\r{label}: {timer_str}", end="")
        time.sleep(1)
        total_seconds -= 1
    
    print(f"\n{label}が終わりました！")

def pomodoro(work_minutes: int, break_minutes: int):
    countdown(work_minutes, "作業")
    print("\n休憩時間です！")
    countdown(break_minutes, "休憩")
    print(f"\n次の作業に戻りましょう！")



if __name__ == "__main__":
    work_minutes = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    break_minutes = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    pomodoro(work_minutes, break_minutes)