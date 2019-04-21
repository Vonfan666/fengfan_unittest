import os,re
#pc电脑路径
apkPath=r'D:\bao\app_2.0.0_beta13_signed.apk'
#直接获取设备名称
deviceName=re.findall('(.+?)\t',os.popen('adb devices').readlines()[1])[0]
#获取安卓版本号
platformVersion=''.join(re.findall('(.+?)',os.popen('adb shell getprop ro.build.version.release').readlines()[0]))
#获取安卓包名
appPackage=re.findall('name=\'(.+?)\'',os.popen('aapt dump badging '+apkPath).readline())[0]
#获取appActivity
appActivity=re.findall('launchable-activity: name=\'(.+?)\'',os.popen('aapt dump badging '+r'D:\bao\app_2.0.0_beta13_signed.apk'+'|findstr "activity"').readline())[0]
global config
config = {}
config['appiumPort']='4723'
config['bootStrapPort']=''
config['seldnroidPort']=''
config['chromiumPort']=''
config['platformName'] = 'Android'
config['platformVersion'] = platformVersion
config['deviceName'] = deviceName
config['appPackage'] = appPackage
config['appActivity']=appActivity
config['noReset'] = True
config['unicodeKeyboard'] = True
config['resetKeyboard'] = True
config['automationName']= 'Uiautomator2'
config['app'] = apkPath
config['newCommandTimeout'] = '400'


global flash
flash = {}
flash['动画xpath']='//android.widget.ImageView'
flash['开始使用id']='com.henji.yunyi.yizhibang:id/guide_bt_go'
flash['首页知道啦id']='com.henji.yunyi.yizhibang:id/mongolia_normal_btn'
flash['我知道啦id']='com.henji.yunyi.yizhibang:id/mongolia_mine_parent_btn'#个人中心引导/
flash['品牌微网知道啦id']='com.henji.yunyi.yizhibang:id/mongolia_promotion_1_know_btn'
flash['允许id']='android:id/button1'
flash['页面返回id']='com.henji.yunyi.yizhibang:id/tv_back'
flash['每日待办知道啦id']='com.henji.yunyi.yizhibang:id/mongolia_normal_btn'
flash['从相册选择id']='com.henji.yunyi.yizhibang:id/tv_dialog_edit_photo_album'
flash['从相册选择确定id']='com.henji.yunyi.yizhibang:id/menu_crop'
flash['确定id']='com.henji.yunyi.yizhibang:id/btn_tips_dialog_confirm'


global bottom
bottom = {}
bottom['首页id'] = 'com.henji.yunyi.yizhibang:id/rl_home_home'
bottom['圈子id'] = 'com.henji.yunyi.yizhibang:id/rl_home_circle'
bottom['消息id'] = 'com.henji.yunyi.yizhibang:id/rl_home_contacts'
bottom['我的id']   = 'com.henji.yunyi.yizhibang:id/rl_home_mine'

global login  #登录页面action
login = {}
login['账号id'] = 'com.henji.yunyi.yizhibang:id/et_login_phone'
login['密码id'] = 'com.henji.yunyi.yizhibang:id/et_login_password'
login['查看密码id']='com.henji.yunyi.yizhibang:id/cb_login_eye_icon'
login['登录id'] = 'com.henji.yunyi.yizhibang:id/btn_login_submit'
login['忘记密码id']='com.henji.yunyi.yizhibang:id/tv_login_forget_password'
login['新用户注册id']='com.henji.yunyi.yizhibang:id/tv_login_register'
login['验证码id'] = 'com.yce.deerstewardphone:id/lay_get_code'
login['验证码文字id'] = 'com.yce.deerstewardphone:id/txt_get_code'

global loginR  #注册页面action
loginR={}
loginR['推荐人易直帮号id']='com.henji.yunyi.yizhibang:id/et_register_referee'
loginR['手机号码id']='com.henji.yunyi.yizhibang:id/et_register_phone'
loginR['验证码输入id']='com.henji.yunyi.yizhibang:id/et_register_verification_code'
loginR['验证码获取id']='com.henji.yunyi.yizhibang:id/btn_register_verification_code'
loginR['密码id']='com.henji.yunyi.yizhibang:id/et_register_password'
loginR['再次输入密码id']='com.henji.yunyi.yizhibang:id/et_register_confirm_password'
loginR['协议id']='com.henji.yunyi.yizhibang:id/cb_register_tick'
loginR['注册id']='com.henji.yunyi.yizhibang:id/btn_register_submit'
loginR['注册xpath']='//android.widget.TextView[@resource-id=\"com.henji.yunyi.yizhibang:id/btn_register_submit\"]'



global banner#轮播图action
banner={}
banner['图1xpath']='//android.widget.LinearLayout[@resource-id=\"com.henji.yunyi.yizhibang:id/loPageTurningPoint\"]/android.widget.ImageView[1]'
banner['图1text']='易直帮2.0版本介绍'
banner['图2xpath']='//android.widget.LinearLayout[@resource-id=\"com.henji.yunyi.yizhibang:id/loPageTurningPoint\"]/android.widget.ImageView[2]'
banner['图2text']='【迈锐宝XL2017款 1.8L 全混动锐尊版报价】2017款 1.8L 全混动锐尊版图片_配置_广西桂海富达-汽车之家'
banner['图3xpath']='//android.widget.LinearLayout[@resource-id=\"com.henji.yunyi.yizhibang:id/loPageTurningPoint\"]/android.widget.ImageView[3]'
banner['图3text']='【丰田车型报价】南宁广缘丰田-汽车之家'


global navigatoin#首页action
navigation={}
navigation['品牌微网xpath']='//android.widget.TextView[@text="品牌微网"]'
navigation['推广软文xpath']='//android.widget.TextView[@text="推广软文"]'
navigation['素材xpath']='//android.widget.TextView[@text="素材"]'
navigation['每日待办xpath']='//android.widget.TextView[@text="每日待办"]'
navigation['营销日记xpath']='//android.widget.TextView[@text="营销日记"]'
navigation['扫一扫xpath']='//android.widget.TextView[@text="扫一扫"]'
navigation['搜人xpath']='//android.widget.TextView[@text="搜人"]'
navigation['群xpath']='//android.widget.TextView[@text="群"]'
navigation['附近的人xpath']='//android.widget.TextView[@text="附近的人"]'
navigation['人脉xpath']='//android.widget.TextView[@text="人脉"]'
navigation['换一批id']='com.henji.yunyi.yizhibang:id/tv_home_exchange'

global  logoV #品牌微网内部元素
logoV={}
logoV['产品介绍xpath']='//android.widget.TextView[@text="产品中心"]'
logoV['产品中心知道啦id']='com.henji.yunyi.yizhibang:id/mongolia_normal_btn'
logoV['品牌微网更多id']='com.henji.yunyi.yizhibang:id/tv_right'
logoV['模板库id']='com.henji.yunyi.yizhibang:id/pop_brand_more_template'
logoV['模板库下一步id']='com.henji.yunyi.yizhibang:id/mongolia_template_library_btn'#模板库知道啦id

global case05#推广软文action
case05={}
case05['我的id']= 'com.henji.yunyi.yizhibang:id/advertorial_mine_article_rab'
case05['返回id']= 'com.henji.yunyi.yizhibang:id/tv_back'
case05['确定id']= 'com.henji.yunyi.yizhibang:id/btn_tips_dialog_confirm'
case05['选择分类id']= 'com.henji.yunyi.yizhibang:id/advertorial_article_category_choose'#下三角
case05['新增文章id']= 'com.henji.yunyi.yizhibang:id/iv_advertorial_article_add'
case05['自编文章xpath']= '//android.widget.TextView[@text=\"自编文章\"]'
case05['外链文章xpath']= '//android.widget.TextView[@text=\"外链生成文章\"]'
case05['保存id']= 'com.henji.yunyi.yizhibang:id/rich_editor_save_btn'
case05['自编文章输入框xpath']= '//android.view.View[@content-desc=\"请输入内容...\"]/android.view.View[1]'
case05['基本信息id']= 'com.henji.yunyi.yizhibang:id/rich_editor_base_info'
case05['添加图片id']= 'com.henji.yunyi.yizhibang:id/rich_editor_title_image_layout'
case05['从相册选择id']= 'com.henji.yunyi.yizhibang:id/tv_dialog_edit_photo_album'
case05['手机图片id']= 'com.henji.yunyi.yizhibang:id/iv_thumb'
case05['选择图片确定id']= 'com.henji.yunyi.yizhibang:id/menu_crop'
case05['文章标题id']= 'com.henji.yunyi.yizhibang:id/rich_editor_title'
case05['文章所属分组id']= 'com.henji.yunyi.yizhibang:id/advertorial_article_category_name'
case05['我的_标题id']= 'com.henji.yunyi.yizhibang:id/advertorial_article_title'
case05['分组class_text']= 'new UiSelector().className("android.widget.TextView").text("分组")'
case05['分组分类id']= 'com.henji.yunyi.yizhibang:id/tv_dialog_group_name'
case05['自定义分组id']= 'com.henji.yunyi.yizhibang:id/tv_dialog_custom'
case05['title_id']= 'com.henji.yunyi.yizhibang:id/tv_title'
case05['添加分组id']= 'com.henji.yunyi.yizhibang:id/add_group_rl'
case05['请输入分组名称id']= 'com.henji.yunyi.yizhibang:id/et_dialog_input_content'
case05['自定义分组管理id']= 'com.henji.yunyi.yizhibang:id/tv_dialog_mine_article_custom'
case05['分组名称id']= 'com.henji.yunyi.yizhibang:id/article_category_name'
case05['分组删除按钮id']= 'com.henji.yunyi.yizhibang:id/iv_item_groups_manager_delete_icon'
case05['删除分组二次确认id']= 'com.henji.yunyi.yizhibang:id/btn_tips_dialog_confirm'
case05['外链输入框id']= 'com.henji.yunyi.yizhibang:id/add_article_editor'

global circle#项目action
circle={}
circle['项目圈id']='com.henji.yunyi.yizhibang:id/college_recommend'
circle['加号id']='com.henji.yunyi.yizhibang:id/floatingActionButton'


global case06 #素材action
case06={}
case06['添加id']='com.henji.yunyi.yizhibang:id/tv_material_ad_add'
case06['微名片id']='com.henji.yunyi.yizhibang:id/material_ad_name_card'
case06['文字id']='com.henji.yunyi.yizhibang:id/material_ad_text'
case06['图片id']='com.henji.yunyi.yizhibang:id/material_ad_image'
case06['视频id']='com.henji.yunyi.yizhibang:id/material_ad_video'
case06['确定id']='com.henji.yunyi.yizhibang:id/btn_tips_dialog_confirm'
case06['外网链接xpath']='//android.widget.TextView[@text="外网链接"]'
case06['名片保存id']='com.henji.yunyi.yizhibang:id/name_card_save'
case06['名片列表id']='com.henji.yunyi.yizhibang:id/name_car_user_name'
case06['头像id']='com.henji.yunyi.yizhibang:id/rl_name_card_avatar_container'
case06['姓名xpath']='//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]'
case06['手机xpath']='//android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.RelativeLayout[1]/android.widget.TextView[1]'
case06['签名xpath']='//android.widget.TextView[@text="个性签名："]'
case06['地址id']='com.henji.yunyi.yizhibang:id/liv_name_card_add_new_address'
case06['公司xpath']='//android.widget.TextView[@text="公司:"]'
case06['微信二维码id']='com.henji.yunyi.yizhibang:id/rl_name_card_qr_code_container'
case06['文字保存id']='com.henji.yunyi.yizhibang:id/save_text_ad'
case06['文字列表id']='com.henji.yunyi.yizhibang:id/text_ad_content'
case06['文字输入框id']='com.henji.yunyi.yizhibang:id/et_text_ad_content'
case06['名片输入框id']='com.henji.yunyi.yizhibang:id/et_dialog_input_content'
case06['名片输入框确定id']='com.henji.yunyi.yizhibang:id/btn_dialog_input_confirm'
case06['外链id']='com.henji.yunyi.yizhibang:id/et_text_ad_link'
case06['图片保存id']='com.henji.yunyi.yizhibang:id/save_image_ad'
case06['图片标题输入框id']='com.henji.yunyi.yizhibang:id/et_image_ad_title'
case06['添加图片id']='com.henji.yunyi.yizhibang:id/image_ad_image_layout'
case06['图片外链id']='com.henji.yunyi.yizhibang:id/et_image_ad_link'
case06['图片list标题id']='com.henji.yunyi.yizhibang:id/image_ad_title'
case06['已添加图片ids']='com.henji.yunyi.yizhibang:id/image_ad_picture'
case06['视频保存id']='com.henji.yunyi.yizhibang:id/save_video_ad'
case06['视频图片id']='com.henji.yunyi.yizhibang:id/video_ad_image_layout'
case06['视频标题id']='com.henji.yunyi.yizhibang:id/et_video_ad_title'
case06['视频外链id']='com.henji.yunyi.yizhibang:id/et_video_ad_link'
case06['视频列表id']='com.henji.yunyi.yizhibang:id/video_ad_title'



global case07
case07={}
case07['新建id']='com.henji.yunyi.yizhibang:id/iv_schedule_calendar_add'
case07['新建保存id']='com.henji.yunyi.yizhibang:id/tv_right'
case07['新建输入框id']='com.henji.yunyi.yizhibang:id/rv_schedule_calendar_content'
case07['新建图片id']='com.henji.yunyi.yizhibang:id/iv_feedback_images_image'
case07['拜访xpath']='//android.widget.TextView[@text="类别"]'
case07['计划开始xpath']='//android.widget.TextView[@text="计划开始时间"]'
case07['开关id']='com.henji.yunyi.yizhibang:id/slide_switch'
case07['重复提醒xpath']='//android.widget.TextView[@text="重复提醒"]'
case07['提前提醒xpath']='//android.widget.TextView[@text="提前提醒"]'
case07['闹钟推迟id']='com.henji.yunyi.yizhibang:id/postpone'
case07['闹钟关闭id']='com.henji.yunyi.yizhibang:id/close'
case07['安卓图片id']='com.henji.yunyi.yizhibang:id/iv_thumb'
case07['安卓图片选择完成id']='com.henji.yunyi.yizhibang:id/btn_ok'
case07['待办区域列表id']='com.henji.yunyi.yizhibang:id/scroll_layout'
case07['日程列表xpath']='//android.widget.LinearLayout[@resource-id=\"com.henji.yunyi.yizhibang:id/right_view_group\"]/android.widget.ImageView[1]'
case07['待办日程id']='com.henji.yunyi.yizhibang:id/schedule_to_do'
case07['历史日程id']='com.henji.yunyi.yizhibang:id/schedule_history'
case07['历史日程列表id']='com.henji.yunyi.yizhibang:id/item_schedule_calendar_content'
case07['删除id']='com.henji.yunyi.yizhibang:id/schedule_delete_btn'
case07['修改id']='com.henji.yunyi.yizhibang:id/schedule_modify_btn'
case07['计划开始确定id']='com.henji.yunyi.yizhibang:id/btnSubmit'



