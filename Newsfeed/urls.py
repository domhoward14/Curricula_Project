from django.conf.urls import patterns, url
from Newsfeed import views

urlpatterns = patterns\
    ('',
        url(r'^$', views.index, name = 'index'),
        url(r'^userRegistration.html/', views.addNewUser, name='addUser'),
        url(r'^studentPage.html/', views.student, name = 'studentPage'),
        url(r'^successfulLike/(?P<slugName>[\w\-]+)/$', views.courseAddLike, name = 'add course like'),
        url(r'^successfulDislike/(?P<slugName>[\w\-]+)/$', views.courseAddDislike, name = 'add course Dislike'),
        url(r'^successfulLessonLike/(?P<slugName>[\w\-]+)/$', views.lessonAddLike, name = 'add course like'),
        url(r'^successfulLessonDislike/(?P<slugName>[\w\-]+)/$', views.lessonAddDislike, name = 'add course Dislike'),
        url(r'^successfulProfessorLike/(?P<slugName>[\w\-]+)/$', views.professorAddLike, name = 'add course like'),
        url(r'^successfulProfessorDislike/(?P<slugName>[\w\-]+)/$', views.professorAddDislike, name = 'add course Dislike'),
        url(r'^professorsPage.html/(?P<slugName>[\w\-]+)/$', views.professor, name = 'professor'),
        url(r'^course/(?P<slugName>[\w\-]+)/$', views.coursePage, name = 'view course page'),
        url(r'^lesson/(?P<slugName>[\w\-]+)/$', views.lessonPage, name = 'view lesson page'),
        url(r'^activate/(?P<slugName>[\w\-]+)/$', views.activateCourse, name = 'activate class'),
        url(r'^adminPage.html/', views.admin, name = 'admin'),
        url(r'^recommendCourse.html/', views.makeRecomendations, name ='recommendations'),
        url(r'^viewAllClasses.html/', views.allClasses, name ='viewAllClasses'),
        url(r'^viewMembers.html/', views.allMembers, name = 'veiwAllMembers'),
        url(r'^success.html/', views.success, name = 'success'),
        url(r'^homePage.html/', views.homePage, name = 'Homepage'),
        url(r'^recommendLesson.html/', views.recLesson, name = 'receccomendLessons'),
    )

