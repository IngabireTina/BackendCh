from employeeapi.viewsets import ItemViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('item', ItemViewset)

# localhost:p/api/employee/5
# GET, POST, PUT, DELETE
# list , retrive