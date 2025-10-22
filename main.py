import sys


# In-memory list to hold tasks
tasks = []


def get_next_id():
	"""Return the next available integer id for a new task."""
	return max((t['id'] for t in tasks), default=0) + 1


def add_task():
	"""Prompt the user to enter a new task and append it to `tasks`.

	Each task is a dict with keys: id, title, description, due_date, completed
	"""
	print("\n-- เพิ่มงานใหม่ --")
	title = input("ชื่อเรื่อง: ").strip()
	if not title:
		print("ชื่อเรื่องห้ามว่าง")
		return
	description = input("รายละเอียด: ").strip()
	due_date = input("วันครบกำหนด (ตัวอย่าง: 2025-10-31): ").strip()

	task = {
		"id": get_next_id(),
		"title": title,
		"description": description,
		"due_date": due_date,
		"completed": False,
	}

	tasks.append(task)
	print(f"เพิ่มงานเรียบร้อย (id={task['id']})")


def view_tasks():
	"""Placeholder: View all tasks"""
	pass


def edit_task():
	"""Placeholder: Edit an existing task"""
	pass


def delete_task():
	"""Placeholder: Delete a task"""
	pass


def print_menu():
	print("\n=== ToDoList CLI ===")
	print("1. เพิ่มงานใหม่")
	print("2. ดูงานทั้งหมด")
	print("3. แก้ไขงาน")
	print("4. ลบงาน")
	print("5. ออกจากโปรแกรม")


def main():
	while True:
		print_menu()
		choice = input("เลือกตัวเลือก (1-5): ").strip()

		if choice == '1':
			add_task()
		elif choice == '2':
			view_tasks()
		elif choice == '3':
			edit_task()
		elif choice == '4':
			delete_task()
		elif choice == '5':
			print("ออกจากโปรแกรม. ลาก่อน!")
			sys.exit(0)
		else:
			print("ตัวเลือกไม่ถูกต้อง กรุณาใส่ตัวเลข 1 ถึง 5")


if __name__ == '__main__':
	main()