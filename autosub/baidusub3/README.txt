����
	1��ƽ̨��linux
	2��python3.6
	3����������װ������pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt


ʹ��˵����
	----Linux
	1��Դ�����/home/share/lmcproject/Task_one/autosub����·���µĲ�ͬ�ļ���Ϊ����һ�Ĳ�ͬ�汾��
	   ���ĵ�ֻ����baidusub3��ʹ�÷�����
	2����linux�µ�ʹ�÷�ʽ���Բ���Linux_API.py   ��Ҫ��һ�¼���Ҫ�㣺
		��һ����Ҫʹ��sys.path.append()��Դ��·������python������·��
		�ڶ���ʹ�� import baidusub3.main as autosub ����ģ��
		��������Ҫ�ƶ���Ҫ������Ļ����Ƶ��·�������·��������·�����ɣ�
		���ģ�ʹ��result = autosub.start(videopath=videopath)��ִ��
		���壺autosub.start(videopath=videopath)������ѡ���������ϸ��Ϣ���Բμ�baidusub3��main.py�к���start()�е�ע��	
		��������������ֵresult Ϊ��Ļ�ļ�����·��

ע��
	1�����ɹ��̻��ڵ�ǰLinux_API.py����·�����ɡ�temp���ļ��У���������м��ļ������������������ʱ�����ļ��л��Զ�ɾ�������ǵ������쳣��ֹ���´μ���ִ��ʱ����Ҫ�ֶ�ɾ����temp���ļ��С�
	2�����ɵ���Ļ�ļ�xxx.srt���ڲ�����������ʱ���ܻ�������������������ֶ��򿪲鿴û�������������bugԭ����δ������ʮ�ֱ�Ǹ������Ӧ�ò�Ӱ���������Խӣ������������ȡ.srt�ļ������쳣���뼰ʱ��ϵ���ǡ�
	






