# Технологии и методы программирования

Лабораторные работы на C++/Python

## Оглавление

- [1 семестр](#1-семестр)
   - [Линейный вычислительный процесс](#Линейный-вычислительный-процесс)
   - [Подпрограммы](#Подпрограммы)
   - [Классы](#Классы)
   - [Конструкторы и деструктор](#Конструкторы-и-деструктор)
   - [Перегрузка операций](#Перегрузка-операций)
   - [Генерация исключений](#Генерация-исключений)
- [2 семестр](#2-семестр)
   - [Наследование](#Наследование)
   - [Интерфейсы](#Интерфейсы)
   - [Разработка калькулятора с использованием среды Qt/PyQt](#Разработка-калькулятора-с-использованием-среды-Qt/PyQt)
- [3 семестр](#3-семестр)
   - [Observer](#Observer)
   - [Simple Factory](#Simple-Factory)

------
## 1 Семестр
#### [:arrow_up:Назад](#Оглавление)
------

#### Линейный вычислительный процесс
Разработать программу на языке С++/Python, выполняющую побитовую конъюнкцию двух битовых строк.
При разработке программы не использовать подпрограммы, классы и т.п., только линейный вычислительный процесс.

[Реализация программы на C++ [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/LinearCPP)\
[Реализация программы на Python [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/LinearPython)

##### [:arrow_up:Назад](#Оглавление)
----

#### Подпрограммы
Модифицировать программу из задания 1, заменив повторяющиеся действия подпрограммами. Добавить работу с файлами.

[Реализация программы на C++ [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/RoutinesCPP)\
[Реализация программы на Python [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/RoutinesPython)

##### [:arrow_up:Назад](#Оглавление)
----

#### Классы
Модифицировать программу из задания 2, создав класс BitString. Все подпрограммы должны быть методами класса BitString.

[Реализация программы на C++ [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/ClassesCPP)\
[Реализация программы на Python [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/ClassesPython)

##### [:arrow_up:Назад](#Оглавление)
----

#### Конструкторы и деструктор
Модифицировать программу из задания 3, заменив статические массивы динамическими. Добавить конструктор по умолчанию, конструктор инициализации, конструктор копирования и деструктор.

[Реализация программы на C++ [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/ConstructAndDestructCPP)\
[Реализация программы на Python [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/ConstructAndDestructPython)

##### [:arrow_up:Назад](#Оглавление)
----

#### Перегрузка операций
Модифицировать программу из задания 4, добавив перегрузку операций присвоения, ввода и вывода, а также операцию конъюнкции

[Реализация программы на C++ [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/OverloadingCPP)\
[Реализация программы на Python [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/OverloadingPython)

##### [:arrow_up:Назад](#Оглавление)
----

#### Генерация исключений
Модифицировать программу из задания 5, добавив генерацию исключений

[Реализация программы на C++ [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/ExceptionsCPP)\
[Реализация программы на Python [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/ExceptionsPython)

##### [:arrow_up:Назад](#Оглавление)
----
------
## 2 Семестр
#### [:arrow_up:Назад](#Оглавление)
------

#### Наследование
На языке С++/Python разработайте три класса, связанные между собой с помощью наследования:
1. Класс Product имеет три поля: название, цена, вес (базовый класс для прочих классов).
2. Класс Buy содержит поля данных: количество купленного товара, суммарная стоимость, суммарный вес (производный класс от класса Product).
3. Класс Check не содержит полей данных. Этот класс должен выводить информацию о продукте и покупке (производный класс от класса Buy).

[Реализация программы на C++ [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/InheritanceCPP)\
[Реализация программы на Python [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/InheritancePython)

##### [:arrow_up:Назад](#Оглавление)
----

#### Интерфейсы
На языке C++/Python реализуйте интерфейс Pet (домашнее животное), задающий следующие методы:
1. setName (задать имя).
2. getName (получить имя).
3. play (играть).

Разработайте три класса домашних животных, реализующих интерфейс Pet.

[Реализация программы на C++ [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/InterfacesCPP)\
[Реализация программы на Python [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/InterfacesPython)

##### [:arrow_up:Назад](#Оглавление)
----

#### Разработка калькулятора с использованием среды Qt/PyQt
Разработать программу Калькулятор с графическим пользовательским интерфейсом на языке С++(Python), используя среду разработки Qt(PyQT).
Критерии качества программы:
1. Для всех кнопок одинакового размера должна совпадать длина и ширина.
2. Для поля ввода/вывода должен быть настроен собственный стиль.
3. Для всех кнопок установлен стиль.
4. Программные названия графических объектов отличаются от названий по умолчанию.
5. Используется отслеживание сигналов нажатия на кнопку.
6. Числа вводятся корректно
7. Десятичная точка вводится корректно
8. Знак числа меняется корректно
9. Кнопка % отрабатывает корректно
10. Корректная работа всех арифметических операций
11. Корректная работа кнопки АС
12. Корректный ввод чисел с нулевой целой частью

[Реализация программы на C++ [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/CalculatorCPP)\
[Реализация программы на Python [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/CalculatorCPP)

##### [:arrow_up:Назад](#Оглавление)
----
------
## 3 Семестр
#### [:arrow_up:Назад](#Оглавление)
-----

#### Observer
Разработайте программу на языке C++/Python, согласно техническому заданию, приведенному в [презентации](https://docs.google.com/presentation/d/1Qv5eilWej9-i1FMI13Si7dirD0_rrTCRCi_HlqTBHT8/edit#slide=id.ge9f31c6a61_0_62).

[Реализация программы на C++ [60 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/ObserverCPP)\
[Реализация программы на Python [100 / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/ObserverPython)

##### [:arrow_up:Назад](#Оглавление)
----
#### Simple Factory
Разработайте программу по управлению пиццерией на языке C++/Python, согласно диаграмме, приведенной в [презентации](https://docs.google.com/presentation/d/1zwbkDw3UY-nLQTUQBQyqr5TfLXpp3VO7lP-jkNFPV2w/edit#slide=id.ge9f3f1777c_0_21).

[Реализация программы на C++ [- / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/ObserverCPP)\
[Реализация программы на Python [- / 100]](https://github.com/RodKingroo/Lab-works-on-TaPM/tree/master/ObserverPython)

##### [:arrow_up:Назад](#Оглавление)
----

(c) 2021-2022 - [Бречка Денис Михайлович](https://vk.com/dbrechka)
Задание выполнены - [Пилипенко Родион](https://github.com/RodKingroo)
