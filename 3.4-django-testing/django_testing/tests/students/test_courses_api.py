import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture()
def api_client():
    return APIClient()

@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):

        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def students_factory():
    def factory(*args, **kwargs):

        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_course(api_client, courses_factory): #проверка получения первого курса (retreve-логика)
    course = courses_factory(name='First Course')
    url = reverse('courses-detail', args=[course.id]) #courses-detail — это строка, представляющая имя маршрута определенный,в urls.py, detail указывает на то, что это запрос для получения данных по конкретному объекту.
    """reverse используется для получения URL-адреса по его имени. 
    позволяет избежать жесткого кодирования URL-адресов, делает его более гибким 
    и удобным для изменения. """
    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data['id'] == course.id
    assert response.data['name'] == course.name

@pytest.mark.django_db
def test_get_all_corses(api_client, courses_factory): #проверка получения курса курса (список-логика)
    courses_list = courses_factory(_quantity=10)
    response = api_client.get("/api/v1/courses/")
    data = response.json()
    assert response.status_code == 200
    assert len(data) == len(courses_list)

@pytest.mark.django_db
def test_filter_courses_by_id(api_client, courses_factory): #проверка фильтра курса курса по id
    courses = courses_factory(_quantity=10)
    target_course = courses[0]
    response = api_client.get(f"/api/v1/courses/?id={target_course.id}")

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['id'] == target_course.id

@pytest.mark.django_db
def test_get_all_corses(api_client, courses_factory): #проверка фильтра списка курсов по name
    course_1 = courses_factory(name='c1')
    response = api_client.get(f"/api/v1/courses/?name={course_1.name}")
    data = response.json()
    assert response.status_code == 200
    assert data[0]['name'] == course_1.name

@pytest.mark.django_db
def test_create_course(api_client): # Проверка создания нового курса
    data = {
        "name": "c1",
        "students": []
    }
    response = api_client.post("/api/v1/courses/", data)

    assert response.status_code == 201
    assert response.data['name'] == data['name']

@pytest.mark.django_db
def test_update_course(api_client, courses_factory):
    course1 = courses_factory(name='Biology')
    new_data = {
        "name": "Biology_2",
        "students": []
    }
    response = api_client.patch(f"/api/v1/courses/{course1.id}/", new_data)

    assert response.status_code == 200
    course1.refresh_from_db()  # Обновляем объект из базы данных
    assert course1.name == new_data['name']

@pytest.mark.django_db
def test_delete_course(api_client, courses_factory):
    course = courses_factory(name="Biology_2")
    url = reverse("courses-detail", args=[course.id])
    response = api_client.delete(url)

    assert response.status_code == 204
    # Проверяем, что курс больше не существует в базе данных
    assert not Course.objects.filter(id=course.id).exists(), "Course was not deleted"







