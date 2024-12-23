import matplotlib.pyplot as plt

def minimal_announcement_times(intervals):
    intervals.sort(key=lambda x: x[1])
    
    announcement_times = []
    last_announcement = None
    
    for start, end in intervals:
        if last_announcement is None or last_announcement < start:
            announcement_times.append(end)
            last_announcement = end
    
    return announcement_times
    
def get_user_input_intervals():

    intervals = []
    print("Enter intervals in the format 'start end' (e.g., 1 4).")
    print("Type 'done' when you are finished.\n")
    
    while True:
        user_input = input("Enter interval (or 'done' to finish): ").strip()
        if user_input.lower() == "done":
            break
        try:
            start, end = map(int, user_input.split())
            if start >= end:
                print("Invalid interval! Start must be less than end.")
            else:
                intervals.append((start, end))
        except ValueError:
            print("Invalid input! Please enter two integers separated by a space.")
    
    return intervals

def plot_intervals_and_announcements(intervals, announcements):
    plt.figure(figsize=(10, 6))
    
    # Plot each interval as a horizontal line at a different y-coordinate
    for i, (start, end) in enumerate(intervals):
        plt.plot([start, end], [i, i], marker='o', color='b', lw=2, label=f"Interval {i+1}" if i == 0 else "")
    
    # Plot minimal announcement times as vertical lines
    for announcement in announcements:
        plt.axvline(x=announcement, color='r', linestyle='--', lw=2, label="Minimal Announcement" if announcements.index(announcement) == 0 else "")
    
    # Adding labels and grid
    plt.title("Intervals and Minimal Announcement Times")
    plt.xlabel("Time")
    plt.ylabel("Intervals")
    plt.grid(True)
    
    # Display the legend
    plt.legend(loc="upper left")
    
    plt.show()
if __name__ == "__main__":

    intervals = get_user_input_intervals()

    if not intervals:
        print("No intervals entered. Exiting program.")
    else:
        result = minimal_announcement_times(intervals)
        print("\nMinimal announcement times:", result)
        # Plot intervals and the minimal announcement times
        plot_intervals_and_announcements(intervals, result)
