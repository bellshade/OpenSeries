import type { Metadata } from "next";
import { Montserrat } from "next/font/google";
import "./globals.css";
import NextTopLoader from "nextjs-toploader";
import Provider from "@/components/Provider";
import Navbar from "@/components/Navbar";

const montserrat = Montserrat({ subsets: ["latin"] });

export const metadata: Metadata = {
    title: "OpenSeries",
    description:
        "Project Untuk Menghitung Segala Jenis Persamaan atau Rumus-Rumus yang terdapat pada bangku sekolah (SMA/SMK/Sederajat). Project ini bertujuan untuk memudahkan siswa dalam menghitung persamaan atau problem-problem yang terdapat pada pelajaran sekolah (cheat egine untuk Sekolah)."
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="en">
            <body className={`${montserrat.className} dark:bg-zinc-800`}>
                <Provider>
                    <Navbar />
                    <NextTopLoader color="#4f46e5" />
                    {children}
                </Provider>
            </body>
        </html>
    );
}
