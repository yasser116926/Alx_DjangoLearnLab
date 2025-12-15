# Social Media API

## Setup

```bash
pip install django djangorestframework pillow
python manage.py migrate
python manage.py runserver


---

## ✔ DELIVERABLES CHECKLIST
- Django project initialized
- Custom User model
- Token authentication implemented
- Registration, login & profile endpoints
- Ready for GitHub push

If you want, I can:
- Add **follow/unfollow logic**
- Add **JWT instead of tokens**
- Prepare **unit tests**
- Review before submission


## Posts & Comments API

### Endpoints
- GET /api/posts/
- POST /api/posts/
- PUT /api/posts/{id}/
- DELETE /api/posts/{id}/

- GET /api/comments/
- POST /api/comments/
- PUT /api/comments/{id}/
- DELETE /api/comments/{id}/

### Features
- Token-based authentication
- Pagination enabled
- Search posts by title or content
- Users can only edit/delete their own posts or comments


## Follow & Feed Functionality

### Follow User
POST /api/accounts/follow/<user_id>/

### Unfollow User
POST /api/accounts/unfollow/<user_id>/

### Feed
GET /api/feed/

The feed displays posts from users that the authenticated user follows, ordered by most recent first.
```
