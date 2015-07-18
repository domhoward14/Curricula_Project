from django.shortcuts import render
from Newsfeed.forms import *
from Newsfeed.models import *

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

def professor(request, slugName):
    Professor = People.objects.get(slug = slugName)
    Courses = course.objects.filter(professor = Professor.first_name)
    context_dict = {'Courses':Courses, 'Professor':Professor}
    return render(request, 'professorsPage.html', context_dict)

def admin(request):
    courses = course.objects.filter(hideBit = 1)
    lessons = lesson.objects.filter(hideBit = 1)
    context_dict = {'courses':courses, 'lessons':lessons}
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

def coursePage(request, slugName):
    Courses = course.objects.get(slug = slugName)
    Lessons = lesson.objects.filter(courseString = Courses.course_name)
    Professor = People.objects.get(first_name=Courses.professor)
    context_dict = {'Courses' : Courses,'Lessons' : Lessons, 'Professor':Professor}
    return render(request, 'course.html', context_dict)

def lessonPage(request, slugName):
    Lesson = lesson.objects.get(slug = slugName)
    Course = course.objects.get(course_name = Lesson.courseString)
    context_dict = {'Lesson' : Lesson, 'Course' : Course}
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



