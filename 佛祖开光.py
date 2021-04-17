import time
from datetime import datetime

print ("""
//
//                          南无啊弥陀佛                            //
//                            _ooOoo_                               //
//                           o8888888o                              //    
//                           88" . "88                              //    
//                           (| ^_^ |)                              //    
//                           O\  =  /O                              //
//                        ____/`---'\____                           //                        
//                      .'  \\|     |//  `.                          //
//                     /  \\|||  :  |||//  \                         //    
//                    /  _||||| -:- |||||-  \                       //
//                    |   | \\\  -  /// |   |                        //
//                    | \_|  ''\---/''  |   |                       //        
//                    \  .-\__  `-`  ___/-. /                       //        
//                  ___`. .'  /--.--\  `. . ___                     //    
//                ."" '<  `.___\_<|>_/___.'  >'"".                  //
//              | | :  `- \`.;`\ _ /`;.`/ - ` : | |                 //    
//              \  \ `-.   \_ __\ /__ _/   .-` /  /                 //
//        ========`-.____`-.___\_____/___.-`____.-'========         //    
//                             `=---='                              //
//        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        //
//         佛祖开光                               永无shell         //
//
""")

while True:
	future = datetime.strptime('2021-04-22 21:00:00','%Y-%m-%d %H:%M:%S')
	now = datetime.now()
	delta = future - now
	hour = delta.seconds/60/60
	minute = (delta.seconds - hour*60*60)/60
	seconds = delta.seconds - hour*60*60 - minute*60
	uin = delta.seconds
	try:
		when_to_stop = abs(int(uin))
	except KeyboardInterrupt:
		break
	while when_to_stop > 0:
		m, s = divmod(when_to_stop, 60)
		h, m = divmod(m, 60)
		time_left = str(h).zfill(2) + "小时" + str(m).zfill(2) + "分" + str(s).zfill(2) + "秒"
		print("            距离**结束还有%d天"%delta.days+time_left+"  我佛慈悲~~~"+ "\r", end="",)
		time.sleep(1)
		when_to_stop -= 1
	print()

