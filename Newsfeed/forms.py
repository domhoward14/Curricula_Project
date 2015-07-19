from django import forms
from Newsfeed.models import People, course, lesson, comment


def getStudents():
    studentList = People.objects.filter(role="Student")
    list=[]
    i =0
    for pupil in studentList:
        name = pupil.first_name
        list.append((str(i), name, ))
        i += 1
    return list

def getCourses():
    classList = course.objects.all()
    list=[]
    for Class in classList:
        name = Class.course_name
        list.append((name, name, ))
    return list

def getLessons():
    classList = lesson.objects.all()
    list=[]
    for Lesson in classList:
        name = Lesson.lesson_name
        list.append((name, name, ))
    return list

def getCourseObj():
    classList = course.objects.all()[0]
    return classList

class NewUserForm(forms.ModelForm):
    role = forms.CharField(widget=forms.HiddenInput(), initial='student')
    first_name = forms.CharField(max_length=128, help_text="Please Enter Your First Name")
    last_name = forms.CharField(max_length=128, help_text="Please Enter Your Last Name")
    email = forms.EmailField(max_length=200, help_text="Please Enter Your Email ")
    phone_number = forms.CharField(max_length=15, help_text="Please enter your phone number")
    hideBit = forms.IntegerField(widget=forms.HiddenInput, initial = 0)
    isActive = forms.IntegerField(widget=forms.HiddenInput, initial = 0)
    password = forms.CharField(max_length=30, help_text="Please enter your password")

    class Meta:
        model = People
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password')

class comments(forms.ModelForm):
    name = forms.CharField(max_length=20, help_text="Name" )
    comment_text = forms.CharField(max_length=250, help_text="Text")
    course = forms.ChoiceField(choices=getCourses())

    class Meta:
        model = comment
        fields = ('name','comment_text', 'course')

class lessComments(forms.ModelForm):
    name = forms.CharField(max_length=20, help_text="Name" )
    comment_text = forms.CharField(max_length=250, help_text="Text")
    course = forms.ChoiceField(choices=getLessons())

    class Meta:
        model = comment
        fields = ('name','comment_text', 'course')


def getList():
        list =[]
        professors = People.objects.filter(role="Professor")
        for teacher in professors:
            name =teacher.first_name
            list.append((name, name,))
        return list

class recommendedClasses(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(recommendedClasses, self).__init__(*args, **kwargs)
        self.fields['professor'] = forms.ChoiceField(choices=getList())

    course_name =forms.CharField(max_length=100, help_text="Please enter the name of the course")
    courseDesc = forms.CharField(max_length=100, help_text="Please enter a description of the course")
    professor = forms.ChoiceField(choices=getList(), help_text="Please choose a  professor from the list")
    courseFee = forms.IntegerField(widget=forms.HiddenInput, initial = 1)
    hideBit = forms.IntegerField(widget=forms.HiddenInput, initial = 1)

    class Meta:
        model = course
        fields = ('course_name', 'courseDesc', 'professor')

class recommendedLessons(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(recommendedLessons, self).__init__(*args, **kwargs)
        self.fields['courseString'] = forms.ChoiceField(choices=getCourses())

    lesson_name = forms.CharField(max_length=100, help_text="Please enter lesson recommendation")
    lessonDesc = forms.CharField(max_length=100, help_text="Please enter lesson description")
    courseString = forms.ChoiceField(getCourses(), help_text="Please choose the corresponding course")

    class Meta:
        model = lesson
        fields = ('lesson_name', 'lessonDesc', 'courseString')






