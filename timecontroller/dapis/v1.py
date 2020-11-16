from dwsl import userservice
from dwsl import forumservice
from dwsl import centerservice

routedict = {
    userservice.CheckUserExist: "/v1/user/signup/",  # 检查同名测试通过
    userservice.AddUser: "/v1/user/signup/",  # 检查增加用户通过
    userservice.UserLogin: "/v1/user/login/",  # 检查登录通过
    userservice.TokenDelete: "/v1/token/delete/",  # 退出系统删除token通过
    userservice.JudgeAnswer: "/v1/user/judgeanswer/",   # 判断密保是否正确 （通过密保修改密码）测试通过
    userservice.ChangePassword: "/v1/user/changepwd/",  # 通过密保修改密码 测试通过
    userservice.ModifyPassword: "/v1/modify/password/",  # 登陆后修改密码成功测试通过
    userservice.ModifyQuestion:"/v1/set/passquestion/",  # 登陆后修改密保成功

    forumservice.ForumDefshow: "/v1/forum/defshow/",  # 论坛首页测试通过
    forumservice.Forumshowme: "/v1/forum/showme/",  # 查看我自己发布的帖子测试通过
    forumservice.PublishForum: "/v1/forum/publish/",  # 发布帖子测试通过
    forumservice.Forumallshow: "/v1/forum/detailshow/",  # 帖子详情测试通过
    forumservice.ForumCommentPublish: "/v1/forum/comment/",  # 评论帖子测试通过
    forumservice.Forumpraise: "/v1/forum/praise/",  # 点赞帖子测试通过
    forumservice.ModifyForum: "/v1/forum/modifyforum/",  # 修改帖子测试通过
    forumservice.DeleteForum: "/v1/forum/deleteforum/",  # 删除帖子测试通过

    centerservice.Personalcencer: "/v1/timecontroller/personalcenter/show/",  # 显示我的个人中心首页测试通过
    centerservice.Ownattention: "/v1/timecontroller/ownattention/show/",  # 查看自己的关注测试通过
    centerservice.CancleAttention: "/v1/timecontroller/cancel/attentionbutton/",  # 取消关注测试成功
    centerservice.OwnFans: "/v1/timecontroller/ownfans/show/",  # 查看自己的粉丝测试通过
    centerservice.Showotherinfo: "/v1/timecontroller/otherinfo/showinfo/",  # 点击他人头像，显示其信息测试通过
    centerservice.AddAttention: "/v1/timecontroller/add/attentionbutton/",  # 关注他人测试通过


}