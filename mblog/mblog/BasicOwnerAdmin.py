from django.contrib import admin

class BasicOwnerAdmin(admin.ModelAdmin):
    '''
    1. 用于自动补充文章、分类、标签、侧边栏、友链等Model的owner字段
    2. 用于针对queryset过滤当前用户的数据（只显示当前用户的数据)
    '''

    exclude = ('owner',)

    def get_queryset(self, request):
        qs = super(BasicOwnerAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BasicOwnerAdmin, self).save_model(request, obj, form, change)