import os
import shutil
def searchs(lists,nexts = '',CWD = os.getcwd()):
	CWD = CWD + nexts
	for i in lists:
		try:
			try:
				if i == "__pycache__":
					shutil.rmtree(CWD + '\\' + i, ignore_errors=False, onerror=None)
			except Exception as e:
				print("D")
				pass
			searchs(os.listdir(CWD + '\\' + i),str('\\'+i), CWD)
		except Exception as e:
			pass
answer = input('Go(Y/N): ')
if answer == 'Y': 
	arrDir = os.listdir(os.getcwd())
	searchs(arrDir)