import sys


def add_task():
	"""Placeholder: Add a new task"""
	pass


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