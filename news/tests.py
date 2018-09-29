from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.hannah= Editor(first_name = 'Hannah', last_name ='Njeri', email ='chegehannah45@gmail.com')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.hannah,Editor))   
    # Testing Save Method
    def test_save_method(self):
        self.hannah.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0) 
    def test_delete_method(self):
        self.hannah.save_editor()
        self.hannah.delete_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) == 0) 
    def test_display_method(self):
        self.hannah.save_editor()
        self.hannah.display_editors()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0) 
    def test_update_method(self):
        self.hannah.save_editor()
        new_editor = Editor.objects.filter(first_name="Hannah").update(first_name="mercy")
        editors=Editor.objects.get(first_name="mercy")
        self.assertTrue(editors.first_name,"mercy")           

class TagTestClass(TestCase):
    def  setUp(self):
        self.hannah= Tag(name ='Hannah') 
# class ArticleTestClass(TestCase):
#     #set up method
#     def setUp(self):
#         hannah= Editor(first_name = 'Hannah', last_name ='Njeri', email ='chegehannah45@gmail.com')
#         hannah.save_editor()
#         self.hannah= Article(title = 'Hannah', post ='anything', editor =hannah) 
#     # Testing  instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.hannah,Article))  
#     # Testing Save Method
#     def test_save_method(self):
#         self.hannah.save_article()
#         articles = Article.objects.all()
#         self.assertTrue(len(articles) > 0)            
class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.hannah= Editor(first_name = 'Hannah', last_name ='Njeri', email ='chegehannah45@gmail.com')
        self.hannah.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.hannah)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)   

    def test_get_news_by_date(self):
        test_date = '2018-09-25'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) > 0)  
        
    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()                        