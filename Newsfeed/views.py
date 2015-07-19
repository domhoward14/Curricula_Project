from django.shortcuts import render
from Newsfeed.forms import *
from Newsfeed.models import *
import datetime

def index(request):
    return render(request, 'Login.html')

def homePage(request):
    return render(request, 'homePage.html')

def activateCourse(request, slugName):
    Class = course.objects.get(slug=slugName)
    Class.hideBit = 0
    Class.courseFee = 100
    Class.save()
    return render(request, 'success.html')

def addNewUser(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return render(request, 'success.html/')

        else:
            print form.errors
    else:
        form = NewUserForm()

    return render(request, 'userRegistration.html', {'form': form})

def makeRecomendations(request):
    if request.method == 'POST':
        form = recommendedClasses(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'success.html/')

        else:
            print form.errors
    else:
        form = recommendedClasses()

    return render(request, 'recommendCourse.html', {'form':form})

def recLesson(request):

    if request.method == 'POST':
        form = recommendedLessons(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'success.html')

        else:
            print form.errors
    else:
        form = recommendedLessons()
        return render(request, 'recommendLesson.html', {'form': form})

def student(request):
    courses = course.objects.order_by('-likes')
    courses = courses.filter(hideBit=0)
    courses = courses[:5]
    people = People.objects.filter(role="Professor")
    people = people[:5]
    lessons = lesson.objects.order_by('-likes')
    lessons = lessons[:5]
    context_dict = {'courses':courses, 'people':people, 'lessons':lessons}
    return render(request, 'studentPage.html', context_dict)

def getProfLikes(Courses):
    list = []
    nameList = []
    i = 0
    for course in Courses:
        list.append([i,course.likes])
        nameList.append(course.course_name)
        i +=2
    return list,nameList

def professor(request, slugName):
    Professor = People.objects.get(slug = slugName)
    Courses = course.objects.filter(professor = Professor.first_name)
    List,NameList = getProfLikes(Courses)
    context_dict = {'Courses':Courses, 'Professor':Professor, 'List':List, 'NameList':NameList}
    return render(request, 'professorsPage.html', context_dict)

def getPopCourseLikes(Courses):
    list = []
    nameList = []
    i = 0
    for course in Courses:
        list.append([i,course.likes])
        nameList.append(course.slug)
        i += 2
    return list,nameList

def admin(request):
    Courses = course.objects.order_by('-likes')[:5]
    List, NameList = getPopCourseLikes(Courses)
    courses = course.objects.filter(hideBit = 1)
    lessons = lesson.objects.filter(hideBit = 1)
    Lessons = lesson.objects.order_by("-likes")[:5]
    context_dict = {'courses':courses, 'lessons':lessons, 'List':List, 'NameList':NameList, 'Lessons':Lessons}
    return render(request, 'adminPage.html', context_dict)

def allClasses(request):
    courses = course.objects.filter(hideBit = 0)
    context_dict = {'courses':courses}
    return render(request, 'viewAllClasses.html', context_dict)

def allMembers(request):
    students = People.objects.filter(role='Student')
    professors = People.objects.filter(role='Professor')
    context_dict = {'students':students, 'professors':professors}
    return render(request, 'viewMembers.html', context_dict)

def success(request):
    return render(request, 'success.html')

def courseAddLike(request, slugName):
    Course = course.objects.get(slug = slugName)
    Course.likes += 1
    Course.save()
    return render(request, 'success.html')

def courseAddDislike(request, slugName):
    Course = course.objects.get(slug = slugName)
    Course.dislikes += 1
    Course.save()
    return render(request, 'success.html')

def updateDb(text, slugName):
    Course = course.objects.filter(slug=slugName)
    Comment = comment.objects.filter(comment_text=text)
    Comment.course = Course.course_name

def coursePage(request, slugName):
    Courses = course.objects.get(slug = slugName)
    Lessons = lesson.objects.filter(courseString = Courses.course_name)
    Professor = People.objects.get(first_name=Courses.professor)
    Comments = comment.objects.filter(course=Courses.course_name)

    if request.method == 'POST':
        form = comments(request.POST)

        if form.is_valid():
            #form.timeStamp = datetime.datetime.today()
            form.save(commit=True)
            return render(request, 'success.html')

        else:
            print form.errors
    else:
        form = comments()
        context_dict = {'Courses' : Courses,'Lessons' : Lessons, 'Professor':Professor, 'Comments':Comments,'form': form}
        return render(request, 'course.html', context_dict)

def lessonPage(request, slugName):
    Lesson = lesson.objects.get(slug = slugName)
    Course = course.objects.get(course_name = Lesson.courseString)
    Comments = comment.objects.filter(course=Lesson.lesson_name)

    if request.method == 'POST':
        form = lessComments(request.POST)

        if form.is_valid():
            #form.timeStamp = datetime.datetime.today()
            form.save(commit=True)
            return render(request, 'success.html')

        else:
            print form.errors
    else:
        form = lessComments()

    context_dict = {'Lesson' : Lesson, 'Course' : Course, 'Comments':Comments,'form': form}
    return render(request, 'LessonPage.html', context_dict)

def lessonAddLike(request, slugName):
    Lesson = lesson.objects.get(slug = slugName)
    Lesson.likes += 1
    Lesson.save()
    return render(request, 'success.html')

def lessonAddDislike(request, slugName):
    Lesson = lesson.objects.get(slug = slugName)
    Lesson.dislikes += 1
    Lesson.save()
    return render(request, 'success.html')

def professorAddLike(request, slugName):
    professor = People.objects.get(slug = slugName)
    professor.likes += 1
    professor.save()
    return render(request, 'success.html')

def professorAddDislike(request, slugName):
    professor = People.objects.get(slug = slugName)
    professor.dislikes += 1
    professor.save()
    return render(request, 'success.html')



