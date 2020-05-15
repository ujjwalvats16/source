use std::io;
#[derive(Debug)]

enum exam{
    pass(i32),
    fail(i32),
}

impl exam{
    fn check(&self,mark_ch:i32)->bool{
        match *self{
            exam::pass(value)=>value>mark_ch,
            exam::fail(value)=>(40-value)<10,
        }
    }
}


fn main(){
    let mark:i32=80;
    println!("please enter pass if you passed else enter fail");
    let mut result=String::new();
    io::stdin().read_line(&mut result).expect("error occured while reading");
    if result.trim()=="pass"{
        println!("please enter score for pass");
    let mut score_pass=String::new();
    io::stdin().read_line(&mut score_pass).expect("error occured while reading");
    let exam_1=exam::pass(score_pass.trim().parse::<i32>().unwrap());
    let x=exam_1.check(mark);
    if x{
        println!("you are eligible for scholarship");
    }
    else{
        
            println!("you are not eligible for scholarship");
        
    }     

    }
    else if result.trim()=="fail"{

    println!("please enter score for fail");
    let mut score_fail=String::new();
    io::stdin().read_line(&mut score_fail).expect("error occured while reading");
    let exam_2=exam::fail(score_fail.trim().parse::<i32>().unwrap());
    let y=exam_2.check(mark);

    if y {
        println!("you are eligible for retest");
    }
    else{ 
        
            println!("you are not eligible for retest");
        
    }
        
    }
    else{
        println!("invalid input");
    }
}