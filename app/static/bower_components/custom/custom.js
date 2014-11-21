var model = {
    user: "Adam",
    //items: [{ action: "Buy Flowers", done: false },
    //    { action: "Get Shoes", done: false },
    //    { action: "Collect Tickets", done: true },
    //    { action: "Call Joe", done: false }]
};

var todoApp = angular.module("todoApp",[]);
todoApp.run(function($http){
   $http.get("static/bower_components/custom/data.json").success(function(data){
       model.items = data;
   })
});
todoApp.filter("checkedItems",function() {
        return function(items,showCompleted){
            var result = [];
            angular.forEach(items,function(item){
                if(item.done == false || showCompleted == true){
                    result.push(item);
                }
            });
            return result;
        };
    });

todoApp.filter("visibleItems",function(){
   var visible = function(items,visibleCompleted){
       var result = [];
       angular.forEach(items,function(item){
          if ( item.done == true || visibleCompleted==true){
              result.push(item);
          }
       });
       return result;
   };
   return visible;
});

todoApp.controller("todoCtrl",function($scope){
        $scope.todo = model;
        $scope.incompleteCount = function() {
            var count = 0;
            angular.forEach($scope.todo.items, function (item) {
                if (!item.done)
                    count++;
            });
            return count;
        };
        $scope.warningLevel = function(){
            return $scope.incompleteCount() < 3 ? "label-success":"label-warning";
        };

        $scope.addnewItem = function(actionText){
            $scope.todo.items.push({action:actionText,done:false});
        };
    }
);