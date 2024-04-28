"use client";
import "./callchecker.css";

import React, { useState } from "react";
import Link from "next/link";
import TheMainPageHeader from "@/widgets/mainPageHeader/TheMainPageHeader";
import { teamList } from "@/data/team";


export default function CC() {
  const [islogin, setislogin] = useState(true);
  return (
    
    <>

      <main className="w-full h-auto deskWide:mx-[calc((100%-1920px)/2)] max-w-[1920px]">
        <div className="pt-[350px] pl-[130px] w-full h-[1080px] callchecker_body">
          <img src="static/robot.svg" className="robotsvg"/>
          <div className="white">
            <h1 className="font-['Montserrat_Alternates'] font-extrabold logotype">CallChecker</h1>
            <h2  className="font-['Montserrat_Alternates'] font-semibold">Бот, предназначенный для оценки качества работы</h2>
            {islogin ? (
            <div>
            <p className="text-[#111111] text-[30px] font-['Montserrat_Alternates'] font-semibold voity">
              Вход
            </p>

            <input
                type="text"
                placeholder="Имя пользователя"
                className="font-['Montserrat_Alternates'] font-semibold inputlogcc"
              />
              <br />
              <input
                type="password"
                placeholder="Пароль"
                className="font-['Montserrat_Alternates'] font-semibold inputlogcc"
              />

            <Link
            href="/signInDuplicate"
            className="flex justify-center items-center mt-[50px] w-[425px] h-[75px] rounded-[50px] vxod"
          >
            <p className="text-[#ffffff] text-[30px] font-['Montserrat_Alternates'] font-medium">
              Войти
            </p>

            <h4 className="font-[Montserrat_Alternates] font-semibold predlogcc">
                Еще нет аккаунта?{" "}
              </h4>
              <button
                  onClick={() => setislogin(false)}
                className="font-[Montserrat_Alternates] font-semibold otvetcc"
              >
                Зарегистрируйтесь!
              </button>
          </Link>
          </div>
          ) : (<div>
<p className="text-[#111111] text-[30px] font-['Montserrat_Alternates'] font-semibold reg">
              Регистрация
            </p>

            <input
                type="text"
                placeholder="Имя пользователя"
                className="font-['Montserrat_Alternates'] font-semibold inputlogccreg"
              />
              <br />
              <input
                type="password"
                placeholder="Пароль"
                className="font-['Montserrat_Alternates'] font-semibold inputlogccreg"
              /><br/>
              <input
                type="email"
                placeholder="Почта"
                className="font-['Montserrat_Alternates'] font-semibold inputlogccreg"
              />


            <Link
            href="/signInDuplicate"
            className="flex justify-center items-center mt-[50px] w-[425px] h-[75px] rounded-[50px] vxodreg"
          >
            <p className="text-[#ffffff] text-[30px] font-['Montserrat_Alternates'] font-medium ppp">
              Продолжить
            </p>

            <h4 className="font-[Montserrat_Alternates] font-semibold predlogccdr">
                Уже есть аккаунт?{" "}
              </h4>
              <button
                  onClick={() => setislogin(true)}
                className="font-[Montserrat_Alternates] font-semibold otvetccdr"
              >
                Войдите
              </button>
          </Link>

          </div>
          )}
          </div>
          </div>
          
      </main>
    </>
  );
}
