
//example 1
////CALLING THE FUCTION BY PASSING STRUCT AS ARGUMENT


/* struct User{
    name:String,
    id:i32,

}


fn main(){

    let user_one=User{
        name:"RONI DAS".to_string(),
        id:123,
    };

    struct_print(user_one);

    println!("the name is {},and id {}",user_one.name,user_one.id);

}

fn struct_print(user_function:User){
    println!("the name is {},and id is {}",user_function.name,user_function.id);
} */

//example 2
//CALLING THE FUCTION WITH A REFERENCE TO STRUCT AS ARGUMENT

struct User{
    name:String,
    id:i32,

}


fn main(){

    let user_one=User{
        name:"RONI DAS".to_string(),
        id:123,
    };

    struct_print(&user_one);

    println!("from main :the name is {},and id {}",user_one.name,user_one.id);

}

fn struct_print(user_function:&User){
    println!("from function :the name is {},and id is {}",user_function.name,user_function.id);
}

