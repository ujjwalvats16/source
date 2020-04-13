//example 1

#[derive(Debug)]
struct User{
        name:String,
        id:i32,
    }
fn main(){

let user_one=User{
    name:"RONI".to_string(),
    id:10,
};
println!("{:?}",user_one); 
  
}


//example 2

#[derive(Debug)]
struct User{
        name:String,
        id:i32,
    }
fn main(){
println!("{:?}",User{name:"RONI".to_string(),id:10}); 
}


//example 3

#[derive(Debug)]
struct User{
        name:String,
        id:i32,
    }
fn main(){
 let user_one=User{
     name:"RONI".to_string(),
     id:10,
     id:100,
 };

println!("{:?}",user_one); 
}
    