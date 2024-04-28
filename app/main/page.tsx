import "./callchecker.css"
import Link from "next/link";
import TheMainPageHeader from "@/widgets/mainPageHeader/TheMainPageHeader";
import { teamList } from "@/data/team";
import React, { useState } from 'react';


export default function CC() {
  return (
    <>

      <main className="w-full h-auto deskWide:mx-[calc((100%-1920px)/2)] max-w-[1920px]">
        <div className="pt-[350px] pl-[130px] w-full h-[1080px] callchecker_body">
          <img src="static/robot.svg" className="robotsvg"/>
          <div className="white">
          <Link
            href="/signInDuplicate"
            className="flex justify-center items-center mt-[50px] w-[425px] h-[75px] rounded-[50px] signto"
          >
            <p className=" text-[25px] font-['Montserrat_Alternates'] font-semibold">
              Войти
            </p>
          </Link>
            <h1 className="font-['Montserrat_Alternates'] font-extrabold logotype">CallChecker</h1>
            <h2  className="font-['Montserrat_Alternates'] font-semibold">Бот, предназначенный для оценки качества работы</h2>
            <h3  className="font-['Montserrat_Alternates'] font-semibold"> Загрузите транскрипцию записи разговоров менеджера и клиентов, чтобы узнать подробности о выполненной работе.</h3>
            <Link
            href="/signInDuplicate"
            className="flex justify-center items-center mt-[50px] w-[425px] h-[75px] rounded-[50px] back"
          >
            <p className="text-[#ffffff] text-[30px] font-['Montserrat_Alternates'] font-medium">
              Попробовать
            </p>

            <img
              src="/static/RightArrowIcon.svg"
              alt=""
              className="ml-[20px]"
            />
          </Link>
          
          </div>
          </div>
          <section className="relative py-[80px] px-[105px] w-full h-[910px] bg-[#151515] rounded-t-[150px] footer">
          <p className="text-[#ffffff] text-[2.5rem] font-['Montserrat'] font-medium">
            made by
          </p>

          <h4 className="mt-[-10px] ml-[-5px] text-[#ffffff] text-[6rem] font-['Montserrat'] font-medium">
            POST ИИрония
          </h4>

          <div className="flex justify-between items-center mt-[50px] w-full h-[380px]">
            {teamList.map((teamMember) => (
              <div
                key={teamMember.id}
                className={`grid justify-items-center ${teamMember.id > 2 ? "w-[320px]" : "w-[250px]"} h-full`}
              >
                <img
                  src={`${teamMember.imageLink}`}
                  alt=""
                  className="w-[200px] h-[200px]"
                />

                <p className="mt-[30px] text-[#ffffff] text-[20px] text-center font-['Montserrat'] font-medium">
                  {teamMember.name}<br/> {teamMember.specialization}
                </p>

                <p className="text-[#ffffff] text-[20px] text-center font-['Montserrat'] font-medium">
                  {teamMember.tgTag}
                </p>
              </div>
            ))}
          </div>

          <p className="absolute bottom-[80px] right-[105px] w-[740px] text-[#8a8a8a] text-[20px] text-right font-['Montserrat'] font-medium text-align">
            Приложение сделано специально <br/>
            для CODEMASTERS INTERNATIONAL на хакатоне TulaHack 2024
          </p>
        </section>
      </main>
    </>
  );
}
