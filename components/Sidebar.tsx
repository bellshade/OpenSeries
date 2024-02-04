"use client";

import { documentations } from "@/constants/documentations";
import { featuredLinks } from "@/constants/featuredLinks";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";

type Props = {};

export default function Sidebar({}: Props) {
    const pathname = usePathname();
    const [isOpen, setIsOpen] = useState(false);

    return (
        <>
            <aside
                className={`fixed inset-y-0 z-20 mt-16 flex min-w-[280px] max-w-[280px] flex-col gap-8 overflow-y-auto border-r bg-inherit p-8 dark:border-r-zinc-800 lg:translate-x-0 ${isOpen ? "translate-x-0" : "-translate-x-full"}`}
            >
                <div className="grid gap-2">
                    {featuredLinks.map((link) => (
                        <Link
                            href={link.href}
                            key={link.name}
                            target={link.target}
                            className="group flex items-center gap-2 font-medium text-zinc-500 hover:text-zinc-800 dark:text-zinc-400 dark:hover:text-zinc-300"
                        >
                            <div
                                className={`grid h-10 w-10 place-items-center rounded-lg ${link.href === pathname ? "bg-indigo-600 text-white" : "bg-indigo-600/10 text-indigo-600 group-hover:bg-indigo-600 group-hover:text-white dark:text-indigo-500"}`}
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
                            <span className="text-xs font-bold uppercase text-zinc-800 dark:text-zinc-200">
                                {documentation.parent}
                            </span>
                            <div className="flex flex-col">
                                {documentation.childs.map((link) => (
                                    <Link
                                        key={link.href}
                                        className={`border-l-2 py-2 pl-6 text-sm font-medium hover:border-l-indigo-600 hover:text-indigo-600 dark:hover:border-l-indigo-500 dark:hover:text-indigo-500 ${link.href === pathname ? "border-l-indigo-600 text-indigo-600 dark:border-l-indigo-500 dark:text-indigo-500" : "text-zinc-400 dark:border-l-zinc-700"}`}
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
                className={`fixed bottom-5 right-5 z-30 flex items-center gap-1 rounded-full bg-zinc-700 px-3 py-3 text-white sm:px-6 lg:hidden`}
            >
                {isOpen ? (
                    <span className="icon-[ph--x] text-2xl"></span>
                ) : (
                    <span className="icon-[ic--round-menu] text-2xl"></span>
                )}
                <span className="hidden text-lg sm:block">{isOpen ? "Close" : "Open"} Sidebar</span>
            </button>
        </>
    );
}
