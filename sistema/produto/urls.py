from .views import *
from django.urls import path


urlpatterns = [
    path('', ProductIndex.as_view(), name='index'),
    path('produto/listar/', ProductList.as_view(), name='all_products'),
    path('produto/<int:product_id>', Product_Single.as_view(), name='product_single'),
    path('produto/criar/', CreateProduct.as_view(), name='create_product'),
    path('produto/editar/<int:product_id>', UpdateProduct.as_view(), name='update_product'),
    path('produto/deletar/<int:product_id>', DeleteProduct.as_view(), name='delete_product'),
    path('criar/comentario/produto/<int:product_id>/<int:user_id>', CreateCommentProduct.as_view(), name='comment_product'),
    path('mural/', CommentPageList.as_view(), name='mural_comment'),
    path('home/', HomeView.as_view(), name='home'),
    path('criar/comentario/page/<int:user_id>', CreateCommentPage.as_view(), name='create_comment_page'),  
]