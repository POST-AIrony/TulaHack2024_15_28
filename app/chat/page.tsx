'use client'
import Link from "next/link";
import React, { useState } from 'react';
      

export default function Home() {
  const [islogin, setislogin] = useState(true)
  return (
    <>
    <div className="w-full h-[1080px]">

      <main className="w-full h-auto">
      <h1 className=" text-[50px] font-['Montserrat_Alternates'] font-extrabold text">
      Привет, пользователь! Это <h2 className="bg-gradient-to-r from-[#9002ff] to-[#ffdb5e] inline-block text-transparent bg-clip-text text-[50px] font-['Montserrat_Alternates'] font-extrabold p-center-two">
            EpicLab
          </h2>
          </h1>
          <h1 className=" text-[40px] font-['Montserrat_Alternates'] font-medium omg"> Чат-бот, сделанный специально для
создания Ваших захватывающих историй.</h1>
        <Link
          href="/chat"
          className="flex justify-center items-center ml-[100px] w-[210px] h-[60px]  font-['Montserrat_Alternates'] font-bold login nachat">
          Начать
        </Link>
        	
      </main>
      </div>
    </>
  );
}
