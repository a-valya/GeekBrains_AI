USE vk;
/* 
1. Пусть задан некоторый пользователь. Из всех пользователей соц. сети найдите человека, 
который больше всех общался с выбранным пользователем (написал ему сообщений).
2. Подсчитать общее количество лайков, которые получили пользователи младше 10 лет..
3. Определить кто больше поставил лайков (всего): мужчины или женщины.
*/

-- № 1 ---------
SELECT count(id), from_user_id, to_user_id 
FROM vk.messages
WHERE to_user_id = 1
GROUP BY from_user_id, to_user_id
ORDER BY count(id) DESC
LIMIT 1;


-- № 2 ---------
SELECT count(id), user_id 
FROM vk.likes 
WHERE user_id IN (SELECT user_id FROM vk.profiles WHERE (TIMESTAMPDIFF(YEAR, birthday, NOW()) < 10 ))
GROUP BY user_id;

-- № 3 ---------
SELECT p.gender, count(l.id)
FROM likes l, profiles p 
GROUP BY p.gender; 
-- ORDER BY count(vk.l.id) DESC 
-- LIMIT 1;

