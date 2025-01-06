class BugTracker:
    def __init__(self):
        self.bugs = []

    def log_bug(self, bug_id, description):
        bug = {"id": bug_id, "description": description, "status": "Open"}
        self.bugs.append(bug)
        print(f"Bug {bug_id} logged: {description}")

    def resolve_bug(self, bug_id):
        for bug in self.bugs:
            if bug["id"] == bug_id:
                bug["status"] = "Resolved"
                print(f"Bug {bug_id} resolved.")
                return
        print(f"Bug {bug_id} not found.")

# Example Usage
tracker = BugTracker()
tracker.log_bug(101, "Device web interface not loading")
tracker.resolve_bug(101)