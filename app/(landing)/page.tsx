"use client";

import Link from "next/link";
import landingImg from "@/assets/landing.png";
import { projectByLinks } from "@/constants/projectByLinks";
import Image from "next/image";

export default function Home() {
    return (
        <>
            <main className="flex min-h-dvh items-center justify-center py-20">
                <div className="container grid items-center gap-10 text-center lg:grid-cols-2 lg:text-left">
                    <div className="order-2 space-y-8 lg:order-1">
                        <h1 className="text-5xl font-black sm:text-8xl lg:text-6xl xl:text-7xl 2xl:text-8xl">
                            <span className="bg-gradient-to-br from-indigo-600 to-rose-400 bg-clip-text text-transparent">
                                OpenSeries:{" "}
                            </span>
                            Cheatsheet Matematika & Fisika
                        </h1>
                        <p className="sm:text-xl sm:leading-relaxed lg:text-lg xl:text-xl">
                            Solusi Pintar untuk Hitung-Hitung Sekolah! Temukan kemudahan mengatasi segala jenis
                            persamaan dan rumus di bangku SMA/SMK/Sederajat.
                        </p>
                        <div className="flex flex-col items-center gap-6 lg:items-start xl:flex-row xl:items-center">
                            <Link
                                className="whitespace-nowrap rounded-md bg-indigo-600 px-8 py-4 font-medium text-white hover:bg-indigo-700"
                                href="/docs"
                            >
                                Get Started
                            </Link>
                            <span className="flex flex-wrap items-center gap-2 text-zinc-500 dark:text-zinc-400">
                                By
                                {projectByLinks.map((link) => (
                                    <Link
                                        key={link.name}
                                        target="_blank"
                                        className="whitespace-nowrap rounded-full border-2 border-rose-400 px-4 py-1 text-xs font-medium text-rose-400 hover:bg-rose-400/20"
                                        href={link.href}
                                    >
                                        {link.name}
                                    </Link>
                                ))}
                            </span>
                        </div>
                    </div>
                    <Image className="order-1 lg:order-2" src={landingImg} alt="" />
                </div>
            </main>
        </>
    );
}
