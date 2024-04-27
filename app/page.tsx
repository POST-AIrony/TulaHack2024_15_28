import Link from "next/link";

import TheMainPageHeader from "@/widgets/mainPageHeader/TheMainPageHeader";
import { teamList } from "@/data/team";

export default function Home() {
  return (
    <>
      <TheMainPageHeader />

      <main className="w-full h-auto deskWide:mx-[calc((100%-1920px)/2)] max-w-[1920px]">
        <div className="pt-[350px] pl-[130px] w-full h-[1080px] bg-[url('/static/MainBackgroundImage.svg')]">
          <h1 className="bg-gradient-to-r from-[#9002ff] to-[#ffdb5e] inline-block text-transparent bg-clip-text text-[8rem] font-['Montserrat_Alternates'] font-extrabold p">
            EpicLab
          </h1>

          <p className="mt-[30px] text-[#ffffff] text-[2.5rem] font-['Montserrat_Alternates'] font-normal w-[50%]">
            Веб-приложение, сделанное для создания, редактирования и
            распространения интерактивных текстовых историй.
          </p>

          <Link
            href="/signIn"
            className="flex justify-center items-center mt-[50px] w-[425px] h-[75px] bg-[#9002ff] rounded-[50px]"
          >
            <p className="text-[#ffffff] text-[2.5rem] font-['Montserrat_Alternates'] font-medium">
              Попробовать
            </p>

            <img
              src="/static/RightArrowIcon.svg"
              alt=""
              className="ml-[20px]"
            />
          </Link>
        </div>

        <section className="relative py-[80px] px-[105px] w-full h-[910px] bg-[#151515] rounded-t-[150px]">
          <p className="text-[#ffffff] text-[2.5rem] font-['Montserrat'] font-medium">
            made by
          </p>

          <h3 className="mt-[-10px] ml-[-5px] text-[#ffffff] text-[6rem] font-['Montserrat'] font-medium">
            POST ИИрония
          </h3>

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
                  {teamMember.name} {teamMember.specialization}
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
