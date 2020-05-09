



//using one argument


struct User{
    age:i32,
    }
    impl User{
    fn display_age(&self)->i32{
    self.age
    }
    }
    fn main(){
    let user_one=User{age:50};
    println!("age is {}",user_one.display_age());
    }
    





//using more than one argument


struct User{
    age:i32,
}

impl User{
    fn eligibility(&self,check_age:i32)->bool{
     self.age>check_age
    }
}

fn main(){
    let check_age:i32=50;
    let user_one=User{age:60};
    let x=user_one.eligibility(check_age);
    if(x){
        println!("age is eligible");
    }
    else{
        println!("age is not eligible");
    }
}
