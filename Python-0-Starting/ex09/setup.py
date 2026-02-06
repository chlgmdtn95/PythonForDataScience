from setuptools import setup

with open('README.md', encoding='utf-8') as f: # README.md 내용 읽어오기
	  long_description = f.read()

setup(
	name='ft_package_hhhh', #module 이름
	version='0.0.0.1', # 버전 등록
	long_description    = long_description, # readme.md 등록
	long_description_content_type = 'text/markdown',  # readme.md 포맷
	description='A sample test package', # 패키지 설명
	author='eagle', # 참여자 등록
	author_email='eagle@42.fr', # 이메일 등록
	url='https://github.com/eagle/ft_package', # url 등록
	license='MIT', # 라이센스 등록
	python_requires='>=3.4', #파이썬 버전 등록
	install_requires=[], # module 필요한 다른 module 등록
	packages=['ft_package_hhhh'] # 업로드할 module이 있는 폴더 입력
)