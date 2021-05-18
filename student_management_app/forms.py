from django import forms 
from django.forms import Form
from student_management_app.models import Courses, SessionYearModel


class DateInput(forms.DateInput):
    input_type = "date"


class AddStudentForm(forms.Form):
    email = forms.EmailField(label="Correo", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Contraseña", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="Nombres", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Apellidos", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Nombre de usuario", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Dirrección", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    #For Displaying Courses
    try:
        courses = Courses.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        course_list = []
    
    #For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
            
    except:
        session_year_list = []
    
    gender_list = (
        ('Hombre','Hombre'),
        ('Mujer','Mujer')
    )

    Blood_type = (
        ('O -', 'O -'),('O +', 'O +'),
        ('A -', 'A -'),('A +', 'A +'),
        ('B -', 'B -'),('B +', 'B +'),
        ('AB -', 'AB -'),('AB +', 'AB +')
    )
    type_etnia = (
        ('Mestizo','Mestizo'),
        ('blanco','blanco'),
        ('indigena','indigena'),
        ('Afroecuatoriano','Afroecuatoriano'),
        ('mulato','mulato')
    )

    course_id = forms.ChoiceField(label="Curso", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Genero", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Año de sesión", choices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
    # session_start_year = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))
    # session_end_year = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Foto de perfil", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))
    disease = forms.CharField(label="Enfermedad", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    Blood_type = forms.ChoiceField(label="Tipo de Sange", choices=Blood_type, widget=forms.Select(attrs={"class":"form-control"}))
    mobile = forms.CharField(label="Celular", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    case_of_emergency = forms.CharField(label="En caso de emergencia llamar a", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    etnia = forms.ChoiceField(label="Genero", choices=type_etnia, widget=forms.Select(attrs={"class":"form-control"}))
    personal_references1 = forms.CharField(label="Referencia personal 1",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references2 = forms.CharField(label="Referencia personal 2",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references3 = forms.CharField(label="Referencia personal 3",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references4 = forms.CharField(label="Referencia personal 4",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references5 = forms.CharField(label="Referencia personal 5",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references6 = forms.CharField(label="Referencia personal 6",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references7 = forms.CharField(label="Referencia personal 7",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references8 = forms.CharField(label="Referencia personal 8",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references9 = forms.CharField(label="Referencia personal 9",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references10 = forms.CharField(label="Referencia personal 10",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))


class EditStudentForm(forms.Form):
    email = forms.EmailField(label="Correo", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="Nombres", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Apellidos", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Nombre de Usuario", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Dirección", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))

    #For Displaying Courses
    try:
        courses = Courses.objects.all()
        course_list = []
        for course in courses:
            single_course = (course.id, course.course_name)
            course_list.append(single_course)
    except:
        course_list = []

    #For Displaying Session Years
    try:
        session_years = SessionYearModel.objects.all()
        session_year_list = []
        for session_year in session_years:
            single_session_year = (session_year.id, str(session_year.session_start_year)+" to "+str(session_year.session_end_year))
            session_year_list.append(single_session_year)
            
    except:
        session_year_list = []

    
    gender_list = (
        ('Hombre','Hombre'),
        ('Mujer','Mujer')
    )

    Blood_type = (
        ('O -', 'O -'),('O +', 'O +'),
        ('A -', 'A -'),('A +', 'A +'),
        ('B -', 'B -'),('B +', 'B +'),
        ('AB -', 'AB -'),('AB +', 'AB +')
    )
    type_etnia = (
        ('Mestizo','Mestizo'),
        ('blanco','blanco'),
        ('indigena','indigena'),
        ('Afroecuatoriano','Afroecuatoriano'),
        ('mulato','mulato')
    )
    
    course_id = forms.ChoiceField(label="Curso", choices=course_list, widget=forms.Select(attrs={"class":"form-control"}))
    gender = forms.ChoiceField(label="Genero", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    session_year_id = forms.ChoiceField(label="Periodo Escolar", choices=session_year_list, widget=forms.Select(attrs={"class":"form-control"}))
    # session_start_year = forms.DateField(label="Session Start", widget=DateInput(attrs={"class":"form-control"}))
    # session_end_year = forms.DateField(label="Session End", widget=DateInput(attrs={"class":"form-control"}))
    profile_pic = forms.FileField(label="Foto de Perfil", required=False, widget=forms.FileInput(attrs={"class":"form-control"}))
    disease = forms.CharField(label="Enfermedad", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    Blood_type = forms.ChoiceField(label="Tipo de Sange", choices=Blood_type, widget=forms.Select(attrs={"class":"form-control"}))
    mobile = forms.CharField(label="Celular", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    case_of_emergency = forms.CharField(label="En caso de emergencia llamar a", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    etnia = forms.ChoiceField(label="Genero", choices=type_etnia, widget=forms.Select(attrs={"class":"form-control"}))
    personal_references1 = forms.CharField(label="Referencia personal 1",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references2 = forms.CharField(label="Referencia personal 2",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references3 = forms.CharField(label="Referencia personal 3",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references4 = forms.CharField(label="Referencia personal 4",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references5 = forms.CharField(label="Referencia personal 5",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references6 = forms.CharField(label="Referencia personal 6",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references7 = forms.CharField(label="Referencia personal 7",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references8 = forms.CharField(label="Referencia personal 8",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references9 = forms.CharField(label="Referencia personal 9",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    personal_references10 = forms.CharField(label="Referencia personal 10",required=False, max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))