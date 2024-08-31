from .views import *
from django.urls import path


urlpatterns = [
    path('index/', ProductIndex.as_view(), name='index'),
    path('listar/', ProductList.as_view(), name='all_products'),
    path('produto/', Product_Single.as_view(), name='product_single'),
    path('criar/', CreateProduct.as_view(), name='create_product'),
    path('editar/<int:product_id>', UpdateProduct.as_view(), name='update_product'),
    path('deletar/<int:product_id>', DeleteProduct.as_view(), name='delete_product'),
    path('mural/', CommentPageList.as_view(), name='mural_comment'),
    path('criar/comentario/<int:user_id>', CreateCommentPage.as_view(), name='create_comment_page'),  
]