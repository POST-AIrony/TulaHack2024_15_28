"use client";
import Link from "next/link";
import React, { useState } from "react";
import { teamList } from "@/data/team";

export default function Home() {
  const [islogin, setislogin] = useState(true);
  return (
    <>
      <main className="w-full h-auto">
        <div className=" w-full h-[1080px] bg-[url('/static/purple.svg')] block-image">
          <h1 className="bg-gradient-to-r from-[#9002ff] to-[#ffdb5e] inline-block text-transparent bg-clip-text text-[8rem] font-['Montserrat_Alternates'] font-extrabold p-center">
            EpicLab
          </h1>
          {islogin ? (
            <div className="bubble anim">
              <h1 className="inline-block text-transparent bg-clip-text text-[8rem] font-['Montserrat_Alternates'] font-extrabold log">
                Вход
              </h1>
              <input
                type="text"
                placeholder="Имя пользователя"
                className="font-['Montserrat_Alternates'] font-extrabold inputlog"
              />
              <br />
              <input
                type="password"
                placeholder="Пароль"
                className="font-['Montserrat_Alternates'] font-extrabold inputlog"
              />

              <Link
                href="/chat"
                className="flex justify-center items-center ml-[100px] w-[210px] h-[60px]  font-['Montserrat_Alternates'] font-medium login button"
              >
                Войти
              </Link>
              <h1 className="font-[Montserrat_Alternates] font-extrabold predlog">
                Еще нет аккаунта?{" "}
              </h1>
              <button
                onClick={() => setislogin(false)}
                className="font-[Montserrat_Alternates] font-extrabold otvet"
              >
                Зарегистрируйтесь!
              </button>
            </div>
          ) : (
            <div className="bubble2 anim">
              <h1 className="inline-block text-transparent bg-clip-text text-[8rem] font-['Montserrat_Alternates'] font-extrabold sig">
                Регистрация
              </h1>
              <input
                type="text"
                placeholder="Имя пользователя"
                className="font-['Montserrat_Alternates'] font-extrabold inputsign"
              />
              <br />
              <input
                type="password"
                placeholder="Пароль"
                className="font-['Montserrat_Alternates'] font-extrabold inputsign"
              />
              <br />
              <input
                type="email"
                placeholder="Почта"
                className="font-['Montserrat_Alternates'] font-extrabold inputsign"
              />

              <Link
                href="/signIn"
                className="flex justify-center items-center ml-[100px] w-[250px] h-[60px]  font-[Montserrat_Alternates] font-medium login button2"
              >
                Продолжить
              </Link>
              <h1 className="font-[Montserrat_Alternates] font-extrabold predlog2">
                Уже есть аккаунт?{" "}
              </h1>
              <button
                onClick={() => setislogin(true)}
                className="font-[Montserrat_Alternates] font-extrabold otvet2"
              >
                Войдите
              </button>
            </div>
          )}
        </div>
      </main>
    </>
  );
}
