"use client";

import { documentations } from "@/constants/documentations";
import { featuredLinks } from "@/constants/featuredLinks";
import { socialLinks } from "@/constants/socialLinks";
import Link from "next/link";
import { usePathname } from "next/navigation";
import React, { useState } from "react";

type Props = {};

export default function Sidebar({}: Props) {
    const pathname = usePathname();
    const [isOpen, setIsOpen] = useState(false);

    return (
        <>
            <aside
                className={`absolute inset-y-0 z-20 flex min-w-[300px] max-w-[300px]  grow flex-col gap-8 overflow-y-auto border-r bg-white p-10 transition-all duration-300 md:static md:translate-x-0 ${isOpen ? "translate-x-0" : "-translate-x-full"}`}
            >
                <header className="flex items-center justify-between border-b pb-3">
                    <Link
                        className="bg-gradient-to-br from-indigo-600 to-rose-400 bg-clip-text font-bold text-transparent"
                        href="/"
                    >
                        OpenSeries
                    </Link>
                    <div className="flex items-center gap-2">
                        {socialLinks.map((link) => (
                            <Link
                                key={link.name}
                                href={link.href}
                                target="_blank"
                                className={`${link.icon} text-xl text-zinc-500 transition-all duration-300 hover:text-indigo-600`}
                            ></Link>
                        ))}
                    </div>
                </header>
                <div className="grid gap-2">
                    {featuredLinks.map((link) => (
                        <Link
                            href={link.href}
                            key={link.name}
                            target={link.target}
                            className="group flex items-center gap-2 font-medium text-zinc-500 transition-all duration-200 hover:text-zinc-800"
                        >
                            <div
                                className={`grid h-10 w-10 place-items-center rounded-lg transition-all duration-200 ${link.href === pathname ? "bg-indigo-600 text-white" : "bg-indigo-100 text-indigo-600 group-hover:bg-indigo-600 group-hover:text-white"}`}
                            >
                                <span className={`${link.icon} text-xl`}></span>
                            </div>
                            {link.name}
                        </Link>
                    ))}
                </div>
                <div className="space-y-4">
                    {documentations.map((documentation) => (
                        <div key={documentation.parent} className="space-y-4">
                            <span className="text-xs font-bold uppercase text-zinc-800">{documentation.parent}</span>
                            <div className="flex flex-col">
                                {documentation.childs.map((link) => (
                                    <Link
                                        key={link.href}
                                        className={`border-l-2 py-2 pl-6 text-sm transition-all duration-200 hover:border-l-indigo-600 hover:text-indigo-600 ${link.href === pathname ? "border-l-indigo-600 text-indigo-600" : "text-zinc-400"}`}
                                        href={link.href}
                                        onClick={() => setIsOpen(false)}
                                    >
                                        {link.title}
                                    </Link>
                                ))}
                            </div>
                        </div>
                    ))}
                </div>
            </aside>
            <button
                onClick={() => setIsOpen(!isOpen)}
                className={`absolute bottom-5 right-5 flex items-center gap-1 rounded-full bg-zinc-800 px-2 py-2 text-white sm:px-6 md:hidden`}
            >
                <span className="hidden sm:block">{isOpen ? "Close" : "Open"} Menu</span>
                {isOpen ? (
                    <span className="icon-[ph--x] text-xl"></span>
                ) : (
                    <span className="icon-[ic--round-menu] text-xl"></span>
                )}
            </button>
        </>
    );
}
