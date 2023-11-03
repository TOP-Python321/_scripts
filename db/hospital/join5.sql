   select d.id,
          concat_ws(' ', last_name, first_name, patr_name) as `врач`,
          v.id
     from doctors as d 
left join vacations as v
       on d.id = v.doctors_id
 order by d.id;

-- +----+-----------------------------------+------+
-- | id | врач                              | id   |
-- +----+-----------------------------------+------+
-- |  1 | Коновалова Василиса Данииловна    |  711 |
-- |  1 | Коновалова Василиса Данииловна    |  712 |
-- |  1 | Коновалова Василиса Данииловна    |  861 |
-- |  2 | Васильева Вероника Артёмовна      |  807 |
-- |  2 | Васильева Вероника Артёмовна      |  834 |
-- |  2 | Васильева Вероника Артёмовна      |  982 |
-- |  3 | Копылова Ульяна Кирилловна        |  732 |
-- |  3 | Копылова Ульяна Кирилловна        |  736 |
-- |  3 | Копылова Ульяна Кирилловна        |  741 |
-- |  3 | Копылова Ульяна Кирилловна        |  813 |
-- |  3 | Копылова Ульяна Кирилловна        |  819 |
-- |  3 | Копылова Ульяна Кирилловна        |  833 |
-- |  3 | Копылова Ульяна Кирилловна        |  839 |
-- |  3 | Копылова Ульяна Кирилловна        |  840 |
-- |  3 | Копылова Ульяна Кирилловна        |  886 |
-- |  3 | Копылова Ульяна Кирилловна        |  921 |
-- |  4 | Дьяконова Екатерина Михайловна    |  685 |
-- |  4 | Дьяконова Екатерина Михайловна    |  726 |
-- |  4 | Дьяконова Екатерина Михайловна    |  762 |
-- |  5 | Егорова Алёна Артёмовна           |  738 |
-- |  5 | Егорова Алёна Артёмовна           |  890 |
-- |  5 | Егорова Алёна Артёмовна           |  956 |
-- |  6 | Гусева Любовь Тимофеевна          |  725 |
-- |  6 | Гусева Любовь Тимофеевна          |  751 |
-- |  6 | Гусева Любовь Тимофеевна          |  788 |
-- |  6 | Гусева Любовь Тимофеевна          |  826 |
-- |  7 | Румянцева Вера Александровна      |  799 |
-- |  7 | Румянцева Вера Александровна      |  812 |
-- |  7 | Румянцева Вера Александровна      |  828 |
-- |  7 | Румянцева Вера Александровна      |  951 |
-- |  8 | Горбачев Дмитрий Александрович    |  944 |
-- |  8 | Горбачев Дмитрий Александрович    |  964 |
-- |  9 | Афанасьев Иван Адамович           |  717 |
-- |  9 | Афанасьев Иван Адамович           |  863 |
-- |  9 | Афанасьев Иван Адамович           |  869 |
-- |  9 | Афанасьев Иван Адамович           |  955 |
-- |  9 | Афанасьев Иван Адамович           |  972 |
-- |  9 | Афанасьев Иван Адамович           |  974 |
-- | 10 | Богданов Михаил Александрович     |  705 |
-- | 10 | Богданов Михаил Александрович     |  801 |
-- | 10 | Богданов Михаил Александрович     |  832 |
-- | 10 | Богданов Михаил Александрович     |  872 |
-- | 10 | Богданов Михаил Александрович     |  897 |
-- | 10 | Богданов Михаил Александрович     |  919 |
-- | 11 | Соколова София Михайловна         |  959 |
-- | 12 | Степанова Александра Денисовна    |  707 |
-- | 12 | Степанова Александра Денисовна    |  723 |
-- | 12 | Степанова Александра Денисовна    |  737 |
-- | 12 | Степанова Александра Денисовна    |  780 |
-- | 12 | Степанова Александра Денисовна    |  818 |
-- | 12 | Степанова Александра Денисовна    |  864 |
-- | 12 | Степанова Александра Денисовна    |  887 |
-- | 13 | Иванова Мария Романовна           |  809 |
-- | 13 | Иванова Мария Романовна           |  817 |
-- | 13 | Иванова Мария Романовна           |  837 |
-- | 14 | Пахомов Марк Михайлович           |  702 |
-- | 14 | Пахомов Марк Михайлович           |  752 |
-- | 14 | Пахомов Марк Михайлович           |  806 |
-- | 14 | Пахомов Марк Михайлович           |  934 |
-- | 14 | Пахомов Марк Михайлович           |  975 |
-- | 15 | Суханов Павел Даниилович          |  778 |
-- | 15 | Суханов Павел Даниилович          |  914 |
-- | 15 | Суханов Павел Даниилович          |  917 |
-- | 15 | Суханов Павел Даниилович          |  973 |
-- | 16 | Лебедев Платон Михайлович         |  753 |
-- | 16 | Лебедев Платон Михайлович         |  981 |
-- | 17 | Воронина Елизавета Сергеевна      |  719 |
-- | 17 | Воронина Елизавета Сергеевна      |  759 |
-- | 17 | Воронина Елизавета Сергеевна      |  775 |
-- | 18 | Романова Анна Владимировна        |  689 |
-- | 18 | Романова Анна Владимировна        |  692 |
-- | 18 | Романова Анна Владимировна        |  739 |
-- | 18 | Романова Анна Владимировна        |  766 |
-- | 18 | Романова Анна Владимировна        |  790 |
-- | 19 | Комаров Дмитрий Тимофеевич        |  770 |
-- | 19 | Комаров Дмитрий Тимофеевич        |  852 |
-- | 19 | Комаров Дмитрий Тимофеевич        |  898 |
-- | 19 | Комаров Дмитрий Тимофеевич        |  958 |
-- | 20 | Кузин Даниил Миронович            |  700 |
-- | 20 | Кузин Даниил Миронович            |  743 |
-- | 20 | Кузин Даниил Миронович            |  843 |
-- | 20 | Кузин Даниил Миронович            |  880 |
-- | 20 | Кузин Даниил Миронович            |  930 |
-- | 20 | Кузин Даниил Миронович            |  936 |
-- | 21 | Журавлева Аделина Степановна      |  757 |
-- | 21 | Журавлева Аделина Степановна      |  871 |
-- | 21 | Журавлева Аделина Степановна      |  960 |
-- | 22 | Савин Родион Михайлович           |  696 |
-- | 22 | Савин Родион Михайлович           |  710 |
-- | 22 | Савин Родион Михайлович           |  728 |
-- | 22 | Савин Родион Михайлович           |  731 |
-- | 22 | Савин Родион Михайлович           |  748 |
-- | 22 | Савин Родион Михайлович           |  802 |
-- | 22 | Савин Родион Михайлович           |  875 |
-- | 22 | Савин Родион Михайлович           |  882 |
-- | 23 | Семенова Полина Владиславовна     |  722 |
-- | 23 | Семенова Полина Владиславовна     |  846 |
-- | 23 | Семенова Полина Владиславовна     |  858 |
-- | 23 | Семенова Полина Владиславовна     |  860 |
-- | 24 | Фролов Даниил Давидович           |  701 |
-- | 24 | Фролов Даниил Давидович           |  976 |
-- | 25 | Сорокин Богдан Степанович         |  690 |
-- | 25 | Сорокин Богдан Степанович         |  825 |
-- | 25 | Сорокин Богдан Степанович         |  879 |
-- | 25 | Сорокин Богдан Степанович         |  902 |
-- | 25 | Сорокин Богдан Степанович         |  983 |
-- | 26 | Баранова Ярослава Никитична       |  688 |
-- | 26 | Баранова Ярослава Никитична       |  708 |
-- | 26 | Баранова Ярослава Никитична       |  827 |
-- | 26 | Баранова Ярослава Никитична       |  854 |
-- | 27 | Миронов Никита Матвеевич          |  896 |
-- | 27 | Миронов Никита Матвеевич          |  910 |
-- | 28 | Березина Николь Владиславовна     |  694 |
-- | 28 | Березина Николь Владиславовна     |  797 |
-- | 28 | Березина Николь Владиславовна     |  908 |
-- | 29 | Никулин Ярослав Михайлович        |  764 |
-- | 29 | Никулин Ярослав Михайлович        |  769 |
-- | 29 | Никулин Ярослав Михайлович        |  811 |
-- | 29 | Никулин Ярослав Михайлович        |  814 |
-- | 29 | Никулин Ярослав Михайлович        |  816 |
-- | 29 | Никулин Ярослав Михайлович        |  820 |
-- | 29 | Никулин Ярослав Михайлович        |  850 |
-- | 29 | Никулин Ярослав Михайлович        |  868 |
-- | 29 | Никулин Ярослав Михайлович        |  962 |
-- | 29 | Никулин Ярослав Михайлович        |  966 |
-- | 30 | Князев Руслан Максимович          |  720 |
-- | 30 | Князев Руслан Максимович          |  859 |
-- | 30 | Князев Руслан Максимович          |  942 |
-- | 30 | Князев Руслан Максимович          |  947 |
-- | 31 | Лобанова Евгения Антоновна        |  777 |
-- | 31 | Лобанова Евгения Антоновна        |  822 |
-- | 32 | Астахова Альбина Максимовна       |  686 |
-- | 32 | Астахова Альбина Максимовна       |  787 |
-- | 32 | Астахова Альбина Максимовна       |  866 |
-- | 33 | Ершова Алиса Александровна        |  697 |
-- | 33 | Ершова Алиса Александровна        |  713 |
-- | 33 | Ершова Алиса Александровна        |  845 |
-- | 33 | Ершова Алиса Александровна        |  878 |
-- | 33 | Ершова Алиса Александровна        |  895 |
-- | 33 | Ершова Алиса Александровна        |  952 |
-- | 34 | Яковлев Иван Константинович       |  824 |
-- | 35 | Парфенова Ева Евгеньевна          |  730 |
-- | 35 | Парфенова Ева Евгеньевна          |  746 |
-- | 35 | Парфенова Ева Евгеньевна          |  776 |
-- | 35 | Парфенова Ева Евгеньевна          |  798 |
-- | 35 | Парфенова Ева Евгеньевна          |  935 |
-- | 35 | Парфенова Ева Евгеньевна          |  943 |
-- | 36 | Шмелева Анна Дмитриевна           |  838 |
-- | 36 | Шмелева Анна Дмитриевна           |  889 |
-- | 36 | Шмелева Анна Дмитриевна           |  913 |
-- | 36 | Шмелева Анна Дмитриевна           |  945 |
-- | 36 | Шмелева Анна Дмитриевна           |  950 |
-- | 36 | Шмелева Анна Дмитриевна           |  968 |
-- | 37 | Андреев Арсений Данилович         |  909 |
-- | 38 | Фокин Владимир Артёмович          |  691 |
-- | 38 | Фокин Владимир Артёмович          |  724 |
-- | 38 | Фокин Владимир Артёмович          |  783 |
-- | 38 | Фокин Владимир Артёмович          |  881 |
-- | 39 | Уткин Тимофей Максимович          |  715 |
-- | 39 | Уткин Тимофей Максимович          |  940 |
-- | 40 | Леонтьева Василиса Львовна        |  727 |
-- | 40 | Леонтьева Василиса Львовна        |  754 |
-- | 40 | Леонтьева Василиса Львовна        |  905 |
-- | 40 | Леонтьева Василиса Львовна        |  929 |
-- | 40 | Леонтьева Василиса Львовна        |  963 |
-- | 40 | Леонтьева Василиса Львовна        |  984 |
-- | 41 | Малахов Глеб Иванович             |  750 |
-- | 41 | Малахов Глеб Иванович             |  761 |
-- | 41 | Малахов Глеб Иванович             |  844 |
-- | 41 | Малахов Глеб Иванович             |  954 |
-- | 41 | Малахов Глеб Иванович             |  969 |
-- | 42 | Андреева Елизавета Денисовна      |  749 |
-- | 42 | Андреева Елизавета Денисовна      |  796 |
-- | 42 | Андреева Елизавета Денисовна      |  877 |
-- | 42 | Андреева Елизавета Денисовна      |  928 |
-- | 43 | Русаков Владимир Ильич            |  734 |
-- | 43 | Русаков Владимир Ильич            |  765 |
-- | 43 | Русаков Владимир Ильич            |  785 |
-- | 43 | Русаков Владимир Ильич            |  795 |
-- | 43 | Русаков Владимир Ильич            |  862 |
-- | 43 | Русаков Владимир Ильич            |  918 |
-- | 43 | Русаков Владимир Ильич            |  931 |
-- | 44 | Дроздов Степан Максимович         | NULL |
-- | 45 | Горюнов Николай Миронович         |  847 |
-- | 45 | Горюнов Николай Миронович         |  980 |
-- | 46 | Малышева Арина Святославовна      |  760 |
-- | 46 | Малышева Арина Святославовна      |  805 |
-- | 46 | Малышева Арина Святославовна      |  810 |
-- | 46 | Малышева Арина Святославовна      |  901 |
-- | 46 | Малышева Арина Святославовна      |  907 |
-- | 46 | Малышева Арина Святославовна      |  949 |
-- | 46 | Малышева Арина Святославовна      |  979 |
-- | 47 | Кузнецова Вероника Ярославовна    |  695 |
-- | 47 | Кузнецова Вероника Ярославовна    |  774 |
-- | 47 | Кузнецова Вероника Ярославовна    |  899 |
-- | 47 | Кузнецова Вероника Ярославовна    |  965 |
-- | 47 | Кузнецова Вероника Ярославовна    |  977 |
-- | 48 | Шишкина Ксения Матвеевна          |  740 |
-- | 48 | Шишкина Ксения Матвеевна          |  782 |
-- | 48 | Шишкина Ксения Матвеевна          |  867 |
-- | 48 | Шишкина Ксения Матвеевна          |  894 |
-- | 48 | Шишкина Ксения Матвеевна          |  924 |
-- | 48 | Шишкина Ксения Матвеевна          |  933 |
-- | 49 | Лебедева Ева Дмитриевна           |  735 |
-- | 49 | Лебедева Ева Дмитриевна           |  755 |
-- | 49 | Лебедева Ева Дмитриевна           |  855 |
-- | 49 | Лебедева Ева Дмитриевна           |  937 |
-- | 50 | Лопатин Марк Даниилович           |  745 |
-- | 50 | Лопатин Марк Даниилович           |  773 |
-- | 51 | Зайцева Таисия Марковна           |  876 |
-- | 51 | Зайцева Таисия Марковна           |  891 |
-- | 52 | Васильева Александра Владимировна |  706 |
-- | 52 | Васильева Александра Владимировна |  771 |
-- | 52 | Васильева Александра Владимировна |  906 |
-- | 52 | Васильева Александра Владимировна |  938 |
-- | 53 | Сухарева Элина Ярославовна        |  763 |
-- | 53 | Сухарева Элина Ярославовна        |  781 |
-- | 53 | Сухарева Элина Ярославовна        |  821 |
-- | 53 | Сухарева Элина Ярославовна        |  856 |
-- | 53 | Сухарева Элина Ярославовна        |  920 |
-- | 53 | Сухарева Элина Ярославовна        |  953 |
-- | 53 | Сухарева Элина Ярославовна        |  961 |
-- | 54 | Долгов Артём Германович           |  698 |
-- | 54 | Долгов Артём Германович           |  699 |
-- | 54 | Долгов Артём Германович           |  718 |
-- | 54 | Долгов Артём Германович           |  793 |
-- | 54 | Долгов Артём Германович           |  803 |
-- | 54 | Долгов Артём Германович           |  823 |
-- | 54 | Долгов Артём Германович           |  841 |
-- | 54 | Долгов Артём Германович           |  885 |
-- | 54 | Долгов Артём Германович           |  948 |
-- | 54 | Долгов Артём Германович           |  970 |
-- | 55 | Фомина Ксения Васильевна          |  716 |
-- | 55 | Фомина Ксения Васильевна          |  815 |
-- | 55 | Фомина Ксения Васильевна          |  853 |
-- | 55 | Фомина Ксения Васильевна          |  892 |
-- | 56 | Миронова Алина Ильинична          |  758 |
-- | 56 | Миронова Алина Ильинична          |  779 |
-- | 56 | Миронова Алина Ильинична          |  830 |
-- | 56 | Миронова Алина Ильинична          |  835 |
-- | 57 | Михайлова Александра Даниэльевна  |  747 |
-- | 57 | Михайлова Александра Даниэльевна  |  842 |
-- | 57 | Михайлова Александра Даниэльевна  |  932 |
-- | 58 | Волкова Ева Егоровна              |  687 |
-- | 58 | Волкова Ева Егоровна              |  756 |
-- | 58 | Волкова Ева Егоровна              |  792 |
-- | 58 | Волкова Ева Егоровна              |  831 |
-- | 58 | Волкова Ева Егоровна              |  865 |
-- | 58 | Волкова Ева Егоровна              |  893 |
-- | 59 | Воробьева Ева Фёдоровна           |  693 |
-- | 59 | Воробьева Ева Фёдоровна           |  704 |
-- | 59 | Воробьева Ева Фёдоровна           |  772 |
-- | 59 | Воробьева Ева Фёдоровна           |  903 |
-- | 59 | Воробьева Ева Фёдоровна           |  916 |
-- | 59 | Воробьева Ева Фёдоровна           |  971 |
-- | 60 | Леонов Егор Матвеевич             |  849 |
-- | 60 | Леонов Егор Матвеевич             |  883 |
-- | 60 | Леонов Егор Матвеевич             |  888 |
-- | 60 | Леонов Егор Матвеевич             |  911 |
-- | 60 | Леонов Егор Матвеевич             |  927 |
-- | 60 | Леонов Егор Матвеевич             |  967 |
-- | 61 | Соколов Андрей Фёдорович          |  873 |
-- | 61 | Соколов Андрей Фёдорович          |  915 |
-- | 62 | Скворцова Елизавета Мирославовна  |  721 |
-- | 62 | Скворцова Елизавета Мирославовна  |  789 |
-- | 62 | Скворцова Елизавета Мирославовна  |  791 |
-- | 63 | Иванов Савва Дмитриевич           |  794 |
-- | 63 | Иванов Савва Дмитриевич           |  804 |
-- | 63 | Иванов Савва Дмитриевич           |  848 |
-- | 63 | Иванов Савва Дмитриевич           |  874 |
-- | 64 | Злобин Илья Алексеевич            |  742 |
-- | 64 | Злобин Илья Алексеевич            |  922 |
-- | 64 | Злобин Илья Алексеевич            |  923 |
-- | 64 | Злобин Илья Алексеевич            |  946 |
-- | 64 | Злобин Илья Алексеевич            |  957 |
-- | 65 | Леонтьев Алексей Константинович   |  729 |
-- | 65 | Леонтьев Алексей Константинович   |  767 |
-- | 65 | Леонтьев Алексей Константинович   |  836 |
-- | 65 | Леонтьев Алексей Константинович   |  925 |
-- | 65 | Леонтьев Алексей Константинович   |  941 |
-- | 65 | Леонтьев Алексей Константинович   |  978 |
-- | 66 | Суслова Ольга Матвеевна           |  703 |
-- | 66 | Суслова Ольга Матвеевна           |  744 |
-- | 66 | Суслова Ольга Матвеевна           |  768 |
-- | 66 | Суслова Ольга Матвеевна           |  784 |
-- | 66 | Суслова Ольга Матвеевна           |  829 |
-- | 66 | Суслова Ольга Матвеевна           |  851 |
-- | 66 | Суслова Ольга Матвеевна           |  900 |
-- | 66 | Суслова Ольга Матвеевна           |  912 |
-- | 66 | Суслова Ольга Матвеевна           |  939 |
-- | 67 | Леонова Татьяна Александровна     |  857 |
-- | 67 | Леонова Татьяна Александровна     |  884 |
-- | 67 | Леонова Татьяна Александровна     |  904 |
-- | 68 | Белов Марк Даниилович             |  709 |
-- | 68 | Белов Марк Даниилович             |  786 |
-- | 68 | Белов Марк Даниилович             |  870 |
-- | 69 | Фомин Константин Андреевич        |  714 |
-- | 69 | Фомин Константин Андреевич        |  808 |
-- | 69 | Фомин Константин Андреевич        |  926 |
-- | 70 | Максимова Алиса Данииловна        |  733 |
-- | 70 | Максимова Алиса Данииловна        |  800 |
-- +----+-----------------------------------+------+
-- 301 rows in set (0.0014 sec)


   select concat_ws(' ', last_name, first_name, patr_name) as `врач`,
          count(v.id) as 'отпусков'
     from doctors as d 
left join vacations as v
       on d.id = v.doctors_id
 group by `врач`
 order by `врач`;

-- +-----------------------------------+----------+
-- | врач                              | отпусков |
-- +-----------------------------------+----------+
-- | Андреев Арсений Данилович         |        1 |
-- | Андреева Елизавета Денисовна      |        4 |
-- | Астахова Альбина Максимовна       |        3 |
-- | Афанасьев Иван Адамович           |        6 |
-- | Баранова Ярослава Никитична       |        4 |
-- | Белов Марк Даниилович             |        3 |
-- | Березина Николь Владиславовна     |        3 |
-- | Богданов Михаил Александрович     |        6 |
-- | Васильева Александра Владимировна |        4 |
-- | Васильева Вероника Артёмовна      |        3 |
-- | Волкова Ева Егоровна              |        6 |
-- | Воробьева Ева Фёдоровна           |        6 |
-- | Воронина Елизавета Сергеевна      |        3 |
-- | Горбачев Дмитрий Александрович    |        2 |
-- | Горюнов Николай Миронович         |        2 |
-- | Гусева Любовь Тимофеевна          |        4 |
-- | Долгов Артём Германович           |       10 |
-- | Дроздов Степан Максимович         |        0 |
-- | Дьяконова Екатерина Михайловна    |        3 |
-- | Егорова Алёна Артёмовна           |        3 |
-- | Ершова Алиса Александровна        |        6 |
-- | Журавлева Аделина Степановна      |        3 |
-- | Зайцева Таисия Марковна           |        2 |
-- | Злобин Илья Алексеевич            |        5 |
-- | Иванов Савва Дмитриевич           |        4 |
-- | Иванова Мария Романовна           |        3 |
-- | Князев Руслан Максимович          |        4 |
-- | Комаров Дмитрий Тимофеевич        |        4 |
-- | Коновалова Василиса Данииловна    |        3 |
-- | Копылова Ульяна Кирилловна        |       10 |
-- | Кузин Даниил Миронович            |        6 |
-- | Кузнецова Вероника Ярославовна    |        5 |
-- | Лебедев Платон Михайлович         |        2 |
-- | Лебедева Ева Дмитриевна           |        4 |
-- | Леонов Егор Матвеевич             |        6 |
-- | Леонова Татьяна Александровна     |        3 |
-- | Леонтьев Алексей Константинович   |        6 |
-- | Леонтьева Василиса Львовна        |        6 |
-- | Лобанова Евгения Антоновна        |        2 |
-- | Лопатин Марк Даниилович           |        2 |
-- | Максимова Алиса Данииловна        |        2 |
-- | Малахов Глеб Иванович             |        5 |
-- | Малышева Арина Святославовна      |        7 |
-- | Миронов Никита Матвеевич          |        2 |
-- | Миронова Алина Ильинична          |        4 |
-- | Михайлова Александра Даниэльевна  |        3 |
-- | Никулин Ярослав Михайлович        |       10 |
-- | Парфенова Ева Евгеньевна          |        6 |
-- | Пахомов Марк Михайлович           |        5 |
-- | Романова Анна Владимировна        |        5 |
-- | Румянцева Вера Александровна      |        4 |
-- | Русаков Владимир Ильич            |        7 |
-- | Савин Родион Михайлович           |        8 |
-- | Семенова Полина Владиславовна     |        4 |
-- | Скворцова Елизавета Мирославовна  |        3 |
-- | Соколов Андрей Фёдорович          |        2 |
-- | Соколова София Михайловна         |        1 |
-- | Сорокин Богдан Степанович         |        5 |
-- | Степанова Александра Денисовна    |        7 |
-- | Суслова Ольга Матвеевна           |        9 |
-- | Суханов Павел Даниилович          |        4 |
-- | Сухарева Элина Ярославовна        |        7 |
-- | Уткин Тимофей Максимович          |        2 |
-- | Фокин Владимир Артёмович          |        4 |
-- | Фомин Константин Андреевич        |        3 |
-- | Фомина Ксения Васильевна          |        4 |
-- | Фролов Даниил Давидович           |        2 |
-- | Шишкина Ксения Матвеевна          |        6 |
-- | Шмелева Анна Дмитриевна           |        6 |
-- | Яковлев Иван Константинович       |        1 |
-- +-----------------------------------+----------+
-- 70 rows in set (0.0020 sec)


   select concat_ws(' ', last_name, first_name, patr_name) as `врач`,
          count(v.id) as `отпусков`
     from doctors as d 
left join vacations as v
       on d.id = v.doctors_id
 group by `врач`
   having `отпусков` = 0
 order by `врач`;

-- +---------------------------+----------+
-- | врач                      | отпусков |
-- +---------------------------+----------+
-- | Дроздов Степан Максимович |        0 |
-- +---------------------------+----------+
-- 1 row in set (0.0020 sec)


select specializations_id, count(*)
from doctors as d
left join specializations_doctors as sd
on d.id = sd.doctors_id
group by specializations_id
having specializations_id is null;

-- +--------------------+----------+
-- | specializations_id | count(*) |
-- +--------------------+----------+
-- |               NULL |       35 |
-- +--------------------+----------+
-- 1 row in set (0.0010 sec)

