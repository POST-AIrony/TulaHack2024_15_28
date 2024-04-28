"use client";
import "./callchecker.css";

import React, { useState } from "react";
import Link from "next/link";
import TheMainPageHeader from "@/widgets/mainPageHeader/TheMainPageHeader";
import { teamList } from "@/data/team";


export default function CC() {
  return (
    
    <>

      <main className="w-full h-auto deskWide:mx-[calc((100%-1920px)/2)] max-w-[1920px]">
        <div className="pt-[350px] pl-[130px] w-full h-[1080px] callchecker_body">
          <div className="whitetrue">
            <h1 className="font-['Montserrat_Alternates'] font-extrabold logotypetrue">CallChecker</h1>
            <Link href="/main" className="exit">
            <img src="static/exit.svg"/>
            </Link>
            <h2  className="font-['Montserrat_Alternates'] font-medium lox">Здравствуйте, пользователь!</h2>
            
            <Link
            href="/signInDuplicate"
            className="flex justify-center items-center mt-[50px] w-[425px] h-[75px] rounded-[50px] backback"
          >
            <p className="text-[#ffffff] text-[30px] font-['Montserrat_Alternates'] font-medium">
              Загрузить транскрибацию
            </p>

            <img
              src="/static/RightArrowIcon.svg"
              alt=""
              className="ml-[20px]"
            />
          </Link>
          

          </div>
          
          </div>
          <div>
          <section className="relative py-[80px] px-[105px] w-full h-[910px] bg-[#151515] rounded-t-[150px] footerfo">
            <h5 className="text-[#ffffff] text-[70px] font-['Montserrat_Alternates'] font-medium podvinut">
              Предыдущие записи
            </h5>
            <div className="page">
<table className="font-['Montserrat_Alternates'] font-medium layout display responsive-table">
    <tbody>

        <tr>
            <td className="organisationnumber">140406</td>
            <td className="organisationname">Stet clita kasd gubergren, no sea takimata sanctus est</td>
            <td className="actions">
                <a href="?" className="edit-item" title="Edit">Edit</a>
                <a href="?" className="remove-item" title="Remove">Remove</a>
            </td>
        </tr>

        <tr>
            <td className="organisationnumber">140412</td>
            <td className="organisationname">Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat</td>
            <td className="actions">
                <a href="?" className="edit-item" title="Edit">Edit</a>
                <a href="?" className="remove-item" title="Remove">Remove</a>
            </td>
        </tr>

        <tr>
            <td className="organisationnumber">140404</td>
            <td className="organisationname">Vel illum dolore eu feugiat nulla facilisis at vero eros</td>
            <td className="actions">
                <a href="?" className="edit-item" title="Edit">Edit</a>
                <a href="?" className="remove-item" title="Remove">Remove</a>
            </td>
        </tr>

        <tr>
            <td className="organisationnumber">140408</td>
            <td className="organisationname">Iusto odio dignissim qui blandit praesent luptatum zzril delenit</td>
            <td className="actions">
                <a href="?" className="edit-item" title="Edit">Edit</a>
                <a href="?" className="remove-item" title="Remove">Remove</a>
            </td>
        </tr>

        <tr>
            <td className="organisationnumber">140410</td>
            <td className="organisationname">
                Lorem ipsum dolor sit amet, consetetur sadipscing elitr, At accusam aliquyam diam
            </td>
            <td className="actions">
                <a href="?" className="edit-item" title="Edit">Edit</a>
                <a href="?" className="remove-item" title="Remove">Remove</a>
            </td>
        </tr>

    </tbody>
</table>
</div>
        </section>
        </div>
      </main>
    </>
  );
}
