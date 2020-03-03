from django.contrib import admin
from django.contrib.admin.models import LogEntry, ADDITION, DELETION
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Tag, Category
from .adminforms import PostAdminForm
from mblog.custom_site import custom_site
from mblog.BasicOwnerAdmin import BasicOwnerAdmin


'''************************** Category *************************'''
class CategoryOwnerFilter(admin.SimpleListFilter):
    '''自定义sidebar的过滤器，只显示当前用户分类'''

    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(id=category_id)
        return queryset

class PostInline(admin.TabularInline):
    fields = ('title', 'desc')
    extra = 1
    model = Post

@admin.register(Category, site=custom_site)
class CategoryAdmin(BasicOwnerAdmin):
    inlines = (PostInline,)
    list_display = ('name', 'status', 'is_nav', 'post_count', 'created_time')
    fields = ('name', 'status', 'is_nav',)
    list_filter = (CategoryOwnerFilter,)

    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'


'''************************** Tag *************************'''
@admin.register(Tag, site=custom_site)
class TagAdmin(BasicOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


'''************************** Post *************************'''
@admin.register(Post, site=custom_site)
class PostAdmin(BasicOwnerAdmin):
    form = PostAdminForm

    list_display = ('title', 'category', 'status', 'owner', 'created_time', 'operator')
    list_display_links = []

    list_filter = (CategoryOwnerFilter,)
    search_fields = ['title', 'category__name']

    actions_on_top = True
    actions_on_bottom = True

    save_on_top = True

    #fields = (( 'title', 'category'),'desc', 'status', 'content', 'tag')
    fieldsets = (  #控制页面布局，格式要求：拥有两个元素的tuple的list
        ('Basic config', {
            'description': 'Basic config desc',
            'fields': ('title', ('category', 'status'),)
        }),
        ('Content', {
            'fields': ('desc', 'content'),
        }),
        ('Extra info', {
            'classes': ('collapse',),
            'fields': ('tag', ),
        })
    )

    filter_horizontal = ('tag', )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    class Media:
        css = {
            'all': ('href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css', ),
        }
        js = ('https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js', )


'''************************** set log *************************'''
@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('object_repr', 'object_id', 'action_flag', 'user', 'change_message', )
    #LogEntry.objects.filter(action_flag=DELETION)
