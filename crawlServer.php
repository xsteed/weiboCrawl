<?php
/*
 * @Descripttion: 服务端脚本
 * @Author: LJZ
 * @Date: 2021-02-05 03:03:02
 * @LastEditTime: 2021-02-05 16:53:06
 */

header("Access-Control-Allow-Origin: *");

function getData()
{
    $servername = "localhost";
    $username = "root";
    $password = "root";
    $db_name = "data";
     
    // 创建连接 可以改用连接池 mysql_pconnect("localhost", "root", "123456");
    $conn = new mysqli($servername, $username, $password,$db_name);

    // 检测连接
    if ($conn->connect_error) 
    {
        die("连接失败: " . $conn->connect_error);
    } 

    $sql = "select * from hot_list ORDER BY uid asc limit 25";
    $result = $conn->query($sql);
    
    $res = array();
    $res[] = [0=>"score",1=> "热度", 2=>"titleName"];

    if ($result->num_rows > 0) {
        header("Content-Type: application/json; charset=UTF-8");
        
        while($row = $result->fetch_array()) {
            
            // 将数据库数据组装成前端能用的格式
            $temp = array();
            $score = ($row['scores']/100000)*rand(1, 2);
            
            if($score<10){
                $temp[] = ($row['scores']/100000)*rand(2, 3);
            }else{
                $temp[] = $score;
            }
            
            $temp[] = $row['scores'];
            $temp[]  = $row['name'];
            $res[] = $temp;
         
        }
        
    }  

    $json = json_encode($res,JSON_UNESCAPED_UNICODE);     
    $conn->close();

    echo $json;
}

getData();