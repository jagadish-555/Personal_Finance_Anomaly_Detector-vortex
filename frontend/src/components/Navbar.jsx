import React from 'react';

export default function Navbar() {
    return (
        <nav className="fixed top-0 w-full z-50 bg-[#09090b]/80 backdrop-blur-xl border-b border-white/5">
            <div className="max-w-[1400px] mx-auto px-6 h-20 flex items-center justify-between">

                {/* Logo Left */}
                <div className="flex-shrink-0 flex items-center gap-2">
                    <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center shadow-[0_0_15px_rgba(99,102,241,0.5)]">
                        <span className="text-white font-bold text-sm tracking-tighter">V</span>
                    </div>
                    <span className="font-bold text-xl tracking-tight text-white">Vortex</span>
                </div>

                {/* Centered Nav Links */}
                <div className="hidden md:flex flex-1 justify-center space-x-10">
                    <a href="#features" className="text-[15px] font-medium text-gray-400 hover:text-white transition-colors">Features</a>
                    <a href="#how-it-works" className="text-[15px] font-medium text-gray-400 hover:text-white transition-colors">How It Works</a>
                    <a href="#pricing" className="text-[15px] font-medium text-gray-400 hover:text-white transition-colors">Pricing</a>
                    <a href="#about" className="text-[15px] font-medium text-gray-400 hover:text-white transition-colors">About</a>
                    <a href="#contact" className="text-[15px] font-medium text-gray-400 hover:text-white transition-colors">Contact</a>
                </div>

                {/* CTA Button Right */}
                <div className="flex-shrink-0 flex items-center">
                    <button className="bg-white/10 hover:bg-white/20 backdrop-blur-md text-white px-6 py-2.5 rounded-full text-[15px] font-medium transition-colors border border-white/10 shadow-[0_4px_14px_0_rgba(255,255,255,0.05)]">
                        Try Now
                    </button>
                </div>

            </div>
        </nav>
    );
}
