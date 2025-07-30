from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """Разрешает изменение объекта только его автору.

    Наследуется от IsAuthenticatedOrReadOnly и добавляет проверку авторства.
    """

    def has_object_permission(self, request, view, obj):
        """Проверяет права доступа к конкретному объекту.

        Args:
            request: Запрос пользователя
            view: Представление, обрабатывающее запрос
            obj: Проверяемый объект

        Returns:
            bool: True если доступ разрешен, False если запрещен
        """
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
