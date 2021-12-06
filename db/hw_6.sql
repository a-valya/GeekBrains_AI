USE vk;
/* 
1. ����� ����� ��������� ������������. �� ���� ������������� ���. ���� ������� ��������, 
������� ������ ���� ������� � ��������� ������������� (������� ��� ���������).
2. ���������� ����� ���������� ������, ������� �������� ������������ ������ 10 ���..
3. ���������� ��� ������ �������� ������ (�����): ������� ��� �������.
*/

-- � 1 ---------
SELECT count(id), from_user_id, to_user_id 
FROM vk.messages
WHERE to_user_id = 1
GROUP BY from_user_id, to_user_id
ORDER BY count(id) DESC
LIMIT 1;


-- � 2 ---------
SELECT count(id), user_id 
FROM vk.likes 
WHERE user_id IN (SELECT user_id FROM vk.profiles WHERE (TIMESTAMPDIFF(YEAR, birthday, NOW()) < 10 ))
GROUP BY user_id;

-- � 3 ---------
SELECT p.gender, count(l.id)
FROM likes l, profiles p 
GROUP BY p.gender; 
-- ORDER BY count(vk.l.id) DESC 
-- LIMIT 1;

