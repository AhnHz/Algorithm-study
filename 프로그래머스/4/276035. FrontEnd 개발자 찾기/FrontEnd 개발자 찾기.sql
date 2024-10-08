SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS D
JOIN SKILLCODES S ON D.SKILL_CODE & S.CODE = S.CODE
WHERE CATEGORY = 'Front End'
GROUP BY ID, EMAIL, FIRST_NAME, LAST_NAME
ORDER BY ID;