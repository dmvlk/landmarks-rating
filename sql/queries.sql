-- 1. Список всех мест
-- SELECT id, name, address FROM places ORDER BY name;

-- 2. Фильтрация: поиск места по подстроке в названии
-- SELECT id, name, address FROM places WHERE name LIKE '%Парк%';

-- 3. Список отзывов с названиями мест и именами авторов
-- SELECT reviews.id, places.name AS place_name, users.name AS user_name, reviews.rating, reviews.comment
-- FROM reviews
-- JOIN places ON reviews.place_id = places.id
-- JOIN users ON reviews.user_id = users.id
-- ORDER BY reviews.id DESC;

-- 4. Средний рейтинг каждого места
-- SELECT places.name, AVG(reviews.rating) AS avg_rating, COUNT(reviews.id) AS review_count
-- FROM places
-- LEFT JOIN reviews ON places.id = reviews.place_id
-- GROUP BY places.id, places.name;

-- 5. Общее количество отзывов
-- SELECT COUNT(*) AS total_reviews FROM reviews;

-- 6. Самые высокооцененные места
-- SELECT places.name, AVG(reviews.rating) AS avg_rating
-- FROM places
-- JOIN reviews ON places.id = reviews.place_id
-- GROUP BY places.id, places.name
-- HAVING AVG(reviews.rating) >= 4.0
-- ORDER BY avg_rating DESC;

-- 7. Отзывы с оценкой 5
-- SELECT * FROM reviews WHERE rating = 5;

-- 8. Сортировка мест по алфавиту
-- SELECT name FROM places ORDER BY name ASC;

-- 9. Пользователи, оставившие больше 1 отзыва
-- SELECT users.name, COUNT(reviews.id) as count
-- FROM users
-- JOIN reviews ON users.id = reviews.user_id
-- GROUP BY users.id, users.name
-- HAVING COUNT(reviews.id) > 1;

-- 10. Места без отзывов
-- SELECT places.name
-- FROM places
-- LEFT JOIN reviews ON places.id = reviews.place_id
-- WHERE reviews.id IS NULL;